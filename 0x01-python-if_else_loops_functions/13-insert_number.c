#include "lists.h"

/**
 * insert_node - Inserts a number into a singly linked list.
 * @head: The head node of a singly linked list.
 * @number: The interger value to be inserted into the list.
 * Return: The new node or NULL in case of failure.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = *head;
	*head = new_node;

	return (NULL);
}
