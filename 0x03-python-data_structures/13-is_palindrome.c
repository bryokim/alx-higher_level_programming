#include "lists.h"
#include <stdio.h>

int size_of_listint(listint_t *head);

/**
 * is_palindrome - check if a listint_t list is a palindrome.
 *
 * @head: ponter to pointer of first node of the list.
 *
 * Return: 0 if the list is not a palindrome, 1 if the list is a palindrome,
 * -1 on fail.
 */
int is_palindrome(listint_t **head)
{
	int total_size, compare_size, idx;
	listint_t *node;

	node = *head;
	total_size = size_of_listint(node);
	if (total_size == 0 || total_size == 1)
		return (1);

	compare_size = total_size / 2;
	int arr[compare_size];

	for (idx = 0; idx < compare_size; idx++)
	{
		arr[idx] = node->n;
		node = node->next;
	}
	/* skip the middle number in odd sized list */
	node = total_size % 2 ? node->next : node;

	for (idx = compare_size - 1; idx >= 0; idx--)
	{
		if (arr[idx] != node->n)
			return (0);
		node = node->next;
	}
	return (1);
}

/**
 * size_of_listint - find number of nodes in a listint_t list.
 *
 * @head: pointer to the head of the list.
 *
 * Return: size of the list.
 */
int size_of_listint(listint_t *head)
{
	int size;
	listint_t *current = head;

	size = 0;
	while (current)
	{
		size++;
		current = current->next;
	}

	return (size);
}
