#include "lists.h"

/**
 * check_cycle - checks singly linked list for a cycle
 * @list: linked list
 * Return: 0 if no cycle else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *node = list;
	int has_cycle = 1;
	int no_cycle = 0;

	while (node->next)
		node = node->next;

		if (node == list)
			return (has_cycle);
	}

	return (no_cycle);
}
