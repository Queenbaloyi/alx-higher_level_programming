#include <stdio.h>
#include <stdlib.h>

struct listint_t {
  int n;
  struct listint_t *next;
};

int is_palindrome(listint_t **head) {
  if (*head == NULL || (*head)->next == NULL) {
    return 1;
  }

  struct listint_t *slow = *head;
  struct listint_t *fast = *head;

  while (fast && fast->next) {
    slow = slow->next;
    fast = fast->next->next;
  }

  if (fast) {
    return 0;
  }

  struct listint_t *prev = NULL;
  struct listint_t *curr = slow->next;

  while (curr) {
    struct listint_t *next = curr->next;
    curr->next = prev;
    prev = curr;
    curr = next;
  }

  while (prev && *head) {
    if (prev->n != (*head)->n) {
      return 0;
    }
    prev = prev->next;
    *head = (*head)->next;
  }

  return 1;
}

int main() {
  struct listint_t *head = malloc(sizeof(struct listint_t));
  head->n = 1;
  head->next = malloc(sizeof(struct listint_t));
  head->next->n = 2;
  head->next->next = malloc(sizeof(struct listint_t));
  head->next->next->n = 1;

  if (is_palindrome(&head)) {
    printf("The list is a palindrome\n");
  } else {
    printf("The list is not a palindrome\n");
  }

  free(head->next->next);
  free(head->next);
  free(head);

  return 0;
}
