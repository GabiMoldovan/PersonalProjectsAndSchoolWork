#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<fcntl.h>
#include<string.h>
#include<sys/wait.h>

int main(int argc, char* argv[]) 
{
    if(argc<3) 
    {
        write(2, "parametru invalid", sizeof("parametru invalid"));
        exit(1);
    }
    char *directory=argv[1];
    int i=2;
    while (i<argc) 
    {
        char *filename = argv[i];
        char path[strlen(directory) + strlen(filename) + 2];
        sprintf(path, "%s/%s.txt", directory, filename);
        // Creare pipe cu nume unic pentru comunicarea intre procese
        char pipe_name[256];
        sprintf(pipe_name, "/tmp/%s_pipe", filename);
        mkfifo(pipe_name, 0666);
        int pid = fork();
        if(pid == 0) 
        {  // procesul copil
            int pipe_fd = open(pipe_name, O_WRONLY);
            if(pipe_fd == -1) 
            {
                write(2, "eroare la pipe", sizeof("eroare la pipe"));
                exit(1);
            }
            int income, cost, mounts = 0, sum = 0, costs = 0;
            FILE *f = fopen(path, "r+");
            if (f == NULL)
            {
                write(2, "parametru invalid", sizeof("parametru invalid"));
                exit(1);
            }
            fscanf(f, "%d", &income);
            while (fscanf(f, "%d", &cost) == 1) costs += cost;
            int emergencyFound = costs * 6;
            int profitPerMount = income - costs;
            if(profitPerMount != 0) 
            {
                if (emergencyFound % profitPerMount == 0) mounts = emergencyFound / profitPerMount;
                else mounts = emergencyFound / profitPerMount + 1;
            }
            fprintf(f, "%d %d\n", emergencyFound, mounts);
            fclose(f);
            // scrierea rezultatelor in pipe
            write(pipe_fd, &emergencyFound, sizeof(int));
            write(pipe_fd, &mounts, sizeof(int));
            close(pipe_fd);
            exit(0);
        } 
        else if(pid > 0) 
        {  // procesul parinte
            int pipe_fd = open(pipe_name, O_RDONLY);
            if (pipe_fd == -1) {
                write(2, "eroare la pipe", sizeof("eroare la pipe"));
                exit(1);
            }
            int emergencyFound, mounts;
            read(pipe_fd, &emergencyFound, sizeof(int));
            read(pipe_fd, &mounts, sizeof(int));
            close(pipe_fd);
            wait(NULL); // se asteapta terminarea procesului copil
        } 
        else 
        {
            write(2, "eroare la fork", sizeof("eroare la fork"));
            exit(1);
        }
        i++;
    }
    return 0;
}
