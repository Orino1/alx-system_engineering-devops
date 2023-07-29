#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
/**
 * infinite_while - Function that runs an infinite loop to simulate
 *                  the parent process.
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - Entry point of the program.
 *
 * Description: Creates 5 zombie processes and displays their PIDs.
 *              The parent process enters an infinite loop to keep running
 *              while the zombie processes are displayed.
 *
 * Return: Always 0.
 */
int main(void)
{
	pid_t child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();

		if (child_pid == -1)
		{
			perror("fork");
			exit(EXIT_FAILURE);
		}
		else if (child_pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(EXIT_SUCCESS);
		}
	}

	infinite_while();

	return (0);
}
