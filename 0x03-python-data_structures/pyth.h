#ifndef PYTH_H
#define PYTH_H

#include <stdio.h>
#include <stdlib.h>

/**
 * pyobj - Python object.
 * @num: A value.
 */
typedef struct pyobj
{
	int num;
} PyObject;

/**
 *  pylist - A struct for pylist.
 *  @base: The base object.
 *  @size: The size allocation.
 */
typedef struct pylist
{
	PyObject base;
	int size;
} PyListObject;

#endif
