#include "lists.h"

/**
 * check_cycle - check if linked list has loop.
 * @list: head of the linked list
 * Return: 0 if there's no loop, 1 if loop is found
 */
int check_cycle(listint_t *list)
{
        listint_t *current, *sec;

        current = sec = list;

        while (current && sec && sec->next)
        {
                current = current->next;
                sec = sec->next->next;

                if (current == sec)
                {
                        return (1);
                }
        }

        return (0);
}
