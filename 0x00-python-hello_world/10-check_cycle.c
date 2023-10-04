#include "lists.h"

/**
 * check_cycle - Checks if the list has a cycle or not.
 * @list: The list to be checked for a cycle.
 * Return: 1 if there is a cycle or 0 if there is no cycle.
 */
int check_cycle(listint_t *list)
{
	int i, step;
	listint_t *slow = list, *fast = list->next;

	if (list == NULL)
		return (0);

	step = 1;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		for (i = 0; i < step; ++i)
		{
			fast = fast->next;
			if (fast == NULL)
				return (0);
		}
		if (slow == fast)
			return (1);
		step *= 2;
	}
	return (0);
}
