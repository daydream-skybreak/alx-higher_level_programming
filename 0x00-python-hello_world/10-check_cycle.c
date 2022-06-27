#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *node1 = list;
	listint_t *node2 = list;

	if (!list)
		return (0);

	while (node1 && node2 && node2->next)
	{
		node1 = node1->next;
		node2 = node2->next->next;
		if (node1 == node2)
			return (1);
	}

	return (0);
}
