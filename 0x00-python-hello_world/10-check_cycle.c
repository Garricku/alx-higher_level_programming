#include "lists.h"

/**
 * check_cycle - Checks if the list has a cycle or not.
 * @list: The list to be checked for a cycle.
 * Return: 1 if there is a cycle or 0 if there is no cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *list_copy = list;

	if (list == NULL)
		return (0);

	while (list_copy != NULL )
	{
		list_copy = list_copy->next->next;
		if (list_copy == NULL)
			break;

		else if (list_copy == list)
			return (1);

	}
	return (0);
}
