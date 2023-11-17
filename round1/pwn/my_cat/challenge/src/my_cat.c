#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

__attribute__((constructor)) void setup(){
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
	setbuf(stderr, NULL);
}

void win(){
    system("/bin/sh");
}

// Signal handler function
void handleCtrlC(int signal) {
    printf("\nCtrl+C pressed. Program terminated.\n");
    exit(1);
}

int main(int argc, char *argv[]) {
    // Set up the Ctrl+C signal handler
    signal(SIGINT, handleCtrlC);

    FILE *file;

    // Check if there are command-line arguments
    if (argc > 1) {
        // Iterate through each provided file and print its contents
        for (int i = 1; i < argc; i++) {
            file = fopen(argv[i], "r");

            // Check if the file can be opened
            if (file == NULL) {
                perror(argv[i]);
                continue;
            }

            // Read and print the contents of the file
            int c;
            while ((c = fgetc(file)) != EOF) {
                putchar(c);
            }

            // Close the file
            fclose(file);
        }
    } else {
        // Read from standard input and print its contents
        char buffer[100];
        while (1){
            fgets(buffer,sizeof(buffer),stdin);
            printf(buffer);
        }
    }

    exit(1);
}
