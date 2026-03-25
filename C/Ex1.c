#include <stdio.h>
#include <time.h>

int main(){
    time_t t;
    struct tm *data;

    time(&t); 
    data = localtime(&t);

    printf("%02d/%02d/%d\n",
            data->tm_mday,
            data->tm_mon + 1,
            data->tm_year + 1900);
    
            return 0;
       
}

