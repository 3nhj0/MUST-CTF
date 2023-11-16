#include <stdio.h>

__attribute__((constructor)) void setup(){
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
	setbuf(stderr, NULL);
}

char* bob(){
    char* name = "Bob";
    return name;
}

void me(){
    system("/bin/sh");
}

int main(){
    char name[30];
    printf("Hello, my name is %s!\n",bob());
    printf("I live at %p\n", &bob);
    printf("What is your name:\n");

    gets(name); // Use fgets instead of gets to avoid buffer overflow

    printf("Nice to meet you, %s!\n", name);
}
