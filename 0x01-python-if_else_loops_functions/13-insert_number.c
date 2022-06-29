#include "lists.h"

/**
 * insert_node - inserts node in a sorted singly linked list
 * @head: the beginning of the singly linked list
 * @number: the value to be inserted in the singly linked list
 *
 * Return: the new singly linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *start = *head, *new;
	new = malloc(sizeof(listint_t));

	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;

	if (start == NULL || start->n >= number)
	{
		new->next = start;
		*head = new;
		return (new);
	}

	while (start && start->next && start->next->n < number)
		start = start->next;

	new->next = start->next;
	start->next = new;

	return (new);
}
