#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - Prints info on python.
 * @p: Pointer to the python object/list.
 * Return: Void/nothing.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated;
	PyObject *item;

	if (!PyList_Check(p))
	{
		printf("Error: Not a Python list.\n");
		return;
	}
	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);
	for (Py_ssize_t i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
