#include "pyth.h"

/**
 * print_python_list_info - Prints info on python.
 * @p: Pointer to the python object/list.
 * Return: Void/nothing.
 */
void print_python_list_info(PyObject *p)
{
	if (p == NULL)
	{
		printf("Error: Not a Python list.\n");
		return;
	}
	PyListObject *list = (PyListObject *)p;
	PyObject *list2 = (PyObject *)p;
	printf("[*] Size of the Python List = %d\n", list->size);
	printf("[*] Allocated = %d\n", list2->num);
}
