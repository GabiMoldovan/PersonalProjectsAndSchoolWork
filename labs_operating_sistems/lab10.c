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
    while(i<argc) 
    {
        int pid = fork();
        if (pid < 0) 
        {
            write(2, "eroare la fork", sizeof("eroare la fork"));
            exit(1);
        } 
        else if(pid == 0) 
        {
            char *filename = argv[i];
            char path[strlen(directory) + strlen(filename) + 2];
            sprintf(path, "%s/%s.txt", directory, filename);
            int pipefd[2];
            if(pipe(pipefd) == -1) 
            {
                write(2, "eroare la pipe", sizeof("eroare la pipe"));
                exit(1);
            }
            int grandchild_pid = fork();
            if(grandchild_pid<0) 
            {
                write(2, "eroare la fork", sizeof("eroare la fork"));
                exit(1);
            } 
            else if(grandchild_pid == 0) 
            { // Procesul nepot
                close(pipefd[0]);  // inchidem capatul de citire al pipe-ului in procesul nepot
                int income, cost, mounts = 0, sum = 0, costs = 0;
                FILE *f = fopen(path, "r+");
                if(f == NULL)
                {
                    write(pipefd[1], "parametru invalid", sizeof("parametru invalid"));
                    exit(1);
                }
                fscanf(f, "%d", &income);
                while(fscanf(f, "%d", &cost) == 1) costs += cost;
                int emergencyFound = costs * 6;
                int profitPerMount = income - costs;
                if(profitPerMount != 0) 
                {
                    if(emergencyFound % profitPerMount == 0) mounts = emergencyFound / profitPerMount;
                    else mounts = emergencyFound / profitPerMount + 1;
                }
                fprintf(f, "%d %d\n", emergencyFound, mounts);
                fclose(f);
                write(pipefd[1], "done", sizeof("done"));  // trimitem un mesaj catre procesul copil
                close(pipefd[1]);  // inchidem capatul de scriere al pipe-ului in procesul nepot
                exit(0);
            } 
            else
            { // procesul copil
                close(pipefd[1]);  // inchidem capatul de scriere al pipe-ului in procesul copil
                char message[256];
                read(pipefd[0], message, sizeof(message));  // asteptam mesajul de la procesul nepot
                if(strcmp(message, "parametru invalid") == 0) 
                {
                    write(2, "parametru invalid", sizeof("parametru invalid"));
                    exit(1);
                }
                close(pipefd[0]); // asteptam ca procesul nepot sa finalizeze
                int status;
                waitpid(grandchild_pid, &status, 0);
                if(WIFEXITED(status)) 
                {
                    if(WEXITSTATUS(status) != 0) 
                    {
                        write(2, "eroare la procesarea fisierului", sizeof("eroare la procesarea fisierului"));
                        exit(1);
                    }
                }
                close(pipefd[0]);  // inchidem capatul de citire al pipe-ului in procesul copil
                exit(0);
            }
        } 
        else 
        { // procesul parinte
            int status;
            waitpid(pid, &status, 0);
            if(WIFEXITED(status)) 
            {
                if(WEXITSTATUS(status) != 0) 
                {
                    write(2, "eroare la fork", sizeof("eroare la fork"));
                    exit(1);
                }
            }
            i++;
        }
    }
    return 0;
}

