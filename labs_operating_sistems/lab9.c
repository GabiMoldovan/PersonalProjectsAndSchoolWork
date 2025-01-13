#include<stdio.h>
#include<stdlib.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<fcntl.h>
#include<dirent.h>
#include<unistd.h>
#include<string.h>

int main(int argc, char* argv[]) 
{
    if(argc<3) 
    {
        write(2, "parametru invalid", sizeof("parametru invalid"));
        exit(1);
        return 0;
    }
    int i=2;
    char *directory = argv[1];
    while(i<argc) 
    {
        int pid=fork();
        if(pid<0) 
        {
            write(2, "eroare la fork", sizeof("eroare la fork"));
            exit(1);
            return 0;
        } 
        else if(pid == 0) 
        {  // copil
            char *filename = argv[i];
            char path[strlen(directory) + strlen(filename) + 2];
            sprintf(path, "%s/%s.txt", directory, filename);
            FILE *file = fopen(path, "r+");
            if (file == NULL) 
            {
                write(2,"parametru invalid",sizeof("parametru invalid"));
                exit(1);
            }
            int salariu, cheltuiala, luni, sumaCheltuieli = 0;
            fscanf(file, "%d", &salariu);
            while(fscanf(file, "%d", &cheltuiala) == 1 ) sumaCheltuieli+=cheltuiala;
            int fondUrgenta = sumaCheltuieli * 6;
            int profit = salariu - sumaCheltuieli;
            if (profit != 0)
            {
                if (fondUrgenta % profit == 0) luni = fondUrgenta/profit;
                else luni = fondUrgenta/profit + 1;
            }
            fprintf(file, "%d %d\n", fondUrgenta, luni);
            fclose(file);
        }
        i++;
    }
    return 0;
}

