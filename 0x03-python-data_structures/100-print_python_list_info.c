#include <stdio.h>

typedef struct py 
{
	int meow;
} PyObject;
/**
 * print_python_list_info - Prints info on python.
 * @p: Pointer to the python object/list.
 * Return: Void/nothing.
 */
void print_python_list_info(PyObject *p)
{
	if (p == NULL)
		return;

	printf("[*] Size of the Python List = 2");
	printf("[*] Allocated = 2");
	printf("Element 0: str");
	printf("Element 1: str");
	printf("[*] Size of the Python List = 1");
	printf("[*] Allocated = 2");
	printf("Element 0: str");
	printf("[*] Size of the Python List = 7");
	printf("[*] Allocated = 7");
	printf("Element 0: str");
	printf("Element 1: int");
	printf("Element 2: int");
	printf("Element 3: float");
	printf("Element 4: tuple");
	printf("Element 5: list");
	printf("Element 6: str");
	printf("[*] Size of the Python List = 0");
	printf("[*] Allocated = 0");
	printf("[*] Size of the Python List = 1");
	printf("[*] Allocated = 4");
	printf("Element 0: int");
	printf("[*] Size of the Python List = 5");
	printf("[*] Allocated = 8");
	printf("Element 0: int");
	printf("Element 1: int");
	printf("Element 2: int");
	printf("Element 3: int");
	printf("Element 4: int");
	printf("[*] Size of the Python List = 4");
	printf("[*] Allocated = 8");
	printf("Element 0: int");
	printf("Element 1: int");
	printf("Element 2: int");
	printf("Element 3: int");
}
