#include <stdio.h>
#include <stdlib.h>

__attribute__((constructor)) void setup(){
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
	setbuf(stderr, NULL);
}

void win() {
    system("/bin/sh");
}

int main() {
    char first_name[30];
    char last_name[30];
    int age;

    puts("Enter your first name:");
    fgets(first_name, sizeof(first_name), stdin);

    puts("Enter your last name:");
    gets(last_name, 80);

    do {
        puts("Enter your age:");
        if (scanf("%d", &age) != 1) {
            puts("Invalid age input. Please enter a valid integer.\n");
            while (getchar() != '\n');
        }
        else if (age < 0 || age > 150) {
            fprintf(stderr, "Invalid age. Please enter an age between 0 and 150.\n");
        }
        else {
            break;
        }
    } while (1);

    printf("Your name is: %s %s\n", first_name, last_name);
    printf("Your age is: %d\n", age);

    printf("Thanks for registering!\n");
    return 0;
}
