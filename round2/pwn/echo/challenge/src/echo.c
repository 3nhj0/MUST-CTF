#include <stdio.h>

__attribute__((constructor)) void setup(){
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
	setbuf(stderr, NULL);
}

int win() {
    system("/bin/sh");
}

int main() {
    char buffer[64];
    
    puts("Welcome to the echo program!");
    puts("Enter some text: ");
    gets(buffer);
    printf(buffer);
    puts("");
    puts("Do you have any reviews?");
    gets(buffer);
    puts("Thanks for using the echo program!");
    return 0;
}
