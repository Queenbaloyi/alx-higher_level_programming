#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 */
typedef struct listint_s
{

int is_palindrome(listint_t **head) {
  if (*head == NULL) {
    return 1;
  }

  listint_t *slow = *head;
  listint_t *fast = *head;

  while (fast != NULL && fast->next != NULL) {
    slow = slow->next;
    fast = fast->next->next;
  }

  // If the list has an odd number of nodes, move the slow pointer one step forward.
  if (fast != NULL) {
    slow = slow->next;
  }

  // Reverse the second half of the list.
  listint_t *prev = NULL;
  listint_t *curr = slow;
  while (curr != NULL) {
    listint_t *next = curr->next;
    curr->next = prev;
    prev = curr;
    curr = next;
  }

  // Compare the first and second halves of the list.
  while (prev != NULL) {
    if (prev->n != *head->n) {
      return 0;
    }
    prev = prev->next;
    *head = *head->next;
  }

  return 1;
}

