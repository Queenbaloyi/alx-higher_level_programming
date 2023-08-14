#include <Python.h>

/**
 * print_python_list_info - Prints some basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p) {
  if (!PyList_Check(p)) {
    printf("Not a list\n");
    return;
  }

  printf("[*] Size of the Python List = %d\n", PyList_Size(p));
  printf("[*] Allocated = %d\n", ((PyListObject *)p)->allocated);

  for (int i = 0; i < PyList_Size(p); i++) {
    PyObject *obj = PyList_GetItem(p, i);
    printf("Element %d: %s\n", i, obj->ob_type->tp_name);
  }
}
