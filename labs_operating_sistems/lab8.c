#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>

int main(int argc, char* argv[])
{
    if (argc<3)
    {
        write(2,"parametru invalid",sizeof("parametru invalid"));
        exit(1);
    }
    char *directory = argv[1];
    int i=2;
    while(i<argc)
    {
        char *filename = argv[i];
        char path[strlen(directory) + strlen(filename) + 2];
        sprintf(path, "%s/%s.txt", directory, filename);
        FILE *f = fopen(path, "r+");
        if (f == NULL) {
            write(2,"parametru invalid",sizeof("parametru invalid"));
            exit(1);
        }
        else
        {
            int income, cost, mounts, sum = 0, costs = 0;
            fscanf(f, "%d", &income);
            while(fscanf(f, "%d", &cost) ==1 ) costs += cost;
            int emergencyFound = costs * 6;
            int profitPerMount = income - costs;
            if (profitPerMount != 0)
            {
                if (emergencyFound % profitPerMount == 0) mounts = emergencyFound/profitPerMount;
                else mounts = emergencyFound/profitPerMount + 1;
            }
            fprintf(f, "%d %d\n", emergencyFound, mounts);
            fclose(f);
        }
        i++;
    }
    return 0;
}
