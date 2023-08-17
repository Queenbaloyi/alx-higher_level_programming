#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

size_t print_dlistint(const dlistint_t *h)
{
  const dlistint_t *current;
  size_t count;

  count = 0;
  for (current = h; current != NULL; current = current->next)
  {
    printf("%d\n", current->n);
    count++;
  }

  return count;
}
