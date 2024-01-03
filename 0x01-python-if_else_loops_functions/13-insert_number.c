#include "lists.h"

/**
 * insert_node - insert node into sorted int list
 * @head: ptr to head of list
 * @number: value to be attached to node
 * Return: ptr to list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *new_node, *prev;

	if (!head)
		return (*head);

	new_node = malloc(sizeof(*head));

	if (!new_node)
		return (new_node);

	new_node->n = number;
	new_node->next = NULL;

	prev = *head;
	curr = (*head)->next;

	while (curr->next)
	{
		if (new_node->n > curr->next->n)
		{
			curr = curr->next;
			prev = prev->next;

			continue;
		}

		new_node->next = curr;
		prev->next = new_node;

		return (*head);
	}

	curr->next = new_node;

	return (*head);
}
