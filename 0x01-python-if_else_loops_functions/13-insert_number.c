#include "lists.h"
#include <stdlib.h>

void add_new_node(listint_t **head, listint_t *new_node);

/**
 * insert_node - inserts a number into a sorted linked list.
 * @head: Head of the linked list.
 * @number: Number to be inserted into the list.
 * Return: Address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;

	if (!*head)
	{
		new_node->next = NULL;
		*head = new_node;
	}
	else
	{
		add_new_node(head, new_node);
	}

	return (new_node);
}

/**
 * add_new_node - adds the new_node to the sorted linked list starting at head.
 * @head: Head of the list to add the new node.
 * @new_node: Node to be adde to the list.
 * Return: void
 */
void add_new_node(listint_t **head, listint_t *new_node)
{
	if (new_node->n > (*head)->n)
	{
		listint_t *temp = *head;

		while (temp->next && new_node->n > temp->n && new_node->n > temp->next->n)
		{
			temp = temp->next;
		}
		new_node->next = temp->next;
		temp->next = new_node;
	}
	else
	{
		new_node->next = *head;
		*head = new_node;
	}
}
