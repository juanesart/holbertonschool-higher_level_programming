#include "lists.h"
/**
 * check_cycle - check if the link list has a cycle
 * @list: list of the linked list
 *
 * Return: 0 if there is no cylce 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *list_h, *list_hnext;

	if (list == NULL || list->next == NULL)
		return (0);
	list_h = list;
	list_hnext = list->next;
	while (list_h != NULL && list_hnext->next != NULL && list_hnext->next->next != NULL)
	{
		if (list_hnext == list_h)
			return (1);
		list_hnext = list_hnext->next->next;
		list_h = list_h->next;
	}
	return (0);
}
