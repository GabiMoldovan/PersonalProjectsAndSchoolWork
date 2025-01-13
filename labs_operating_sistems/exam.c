#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/stat.h>
#include<sys/types.h>
#include<fcntl.h>

int main(int argc, char* argv[])
{
    if(argc<2)
    {
        write(2, "parametru invalid", sizeof("parametru invalid"));
        exit(1);
    }
    char* linie[101];
    char* file=argv[1];
    FILE* f=fopen(file, "r");
    //printf("%s", file);
    char line[101];
    int pid;
    int rez;
    int nr1=0, nr2=0;
    while(fgets(line, sizeof(line), f))
    {
        //pid=fork();
        if(pid<0)
        {
            write(2, "eroare la fork", sizeof("eroare la fork"));
            exit(1);
        }
        if(pid==0)
        {
            int i=0;
            nr1=0;
            nr2=0;
            while(line[i]!=' ') nr1=(nr1*10 + line[i]-'0'), i++;
            i++;
            while(line[i]!=' ') nr2=(nr2*10 + line[i]-'0'), i++;
            rez = nr1*3 + nr2;
            printf("%d\n", rez);
            pid=fork();
        }
        if(pid==1)
        {
            //printf("%d\n", rez);
        }
    }
    fclose(f);
    return 0;
}
