#include "lists.h"
/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: First node in the singly linked list.
 * Return: 0 if it is not a palindrone and 1 if it is a palindrone.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current_node = *head;
	int *copy_list, len = 0, i = 0;

	if (head == NULL || *head == NULL)
		return (1);

	while (current_node != NULL)
	{
		len++;
		current_node = current_node->next;
	}
	copy_list = malloc(sizeof(int) * len);
	if (copy_list == NULL)
		return (0);

	current_node = *head;
	for (i = 0; i < len; i++)
	{
		copy_list[i] = current_node->n;
		current_node = current_node->next;
	}
	for (i = 0; i < len / 2; i++)
	{
		if (copy_list[i] != copy_list[(len - 1) - i])
		{
			free(copy_list);
			return (0);
		}
	}
	free(copy_list);
	return (1);
}
