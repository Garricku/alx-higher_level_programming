#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints Python info
 * @p: The python object
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}

/**
 * print_python_bytes - Prints Python info
 * @p: The python object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t size = PyBytes_GET_SIZE(p);
	char *str = PyBytes_AsString(p);
	Py_ssize_t i;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size > 10)
		size = 10;
	printf("  first %ld bytes:", size);
	for (i = 0; i < size; i++)
		printf(" %02x", (unsigned char)str[i]);
	printf("\n");
}

/**
 * print_python_float - Prints Python info
 * @p: The python object
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *f = (PyFloatObject *)p;
	double d;

	printf("[.] float object info\n");

	if (!PyFloat_Check(f))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

#if PY_MAJOR_VERSION >= 3
	d = ((PyFloatObject *)f)->ob_fval;
#else
	d = f->ob_fval;
#endif
	printf("  value: %lf\n", d);
}
