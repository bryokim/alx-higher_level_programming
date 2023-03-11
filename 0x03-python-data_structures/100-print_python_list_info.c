#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include <stdio.h>

/**
 * print_type_str - print the type of the item
 *
 * @item: item to get type
 */
void print_type_str(PyObject *item)
{
	char *str;

	if (PyFloat_Check(item))
		str = "float\n";
	else if (PyLong_Check(item))
		str = "int\n";
	else if (PyList_Check(item))
		str = "list\n";
	else if (PyTuple_Check(item))
		str = "tuple\n";
	else
		str = "str\n";

	printf("%s", str);
}

/**
 * print_python_list_info - print info about a Python list.
 *
 * @p: PyObject representing a Python list.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t idx, len;
	PyObject *item;

	/* If p is not a list or an instance of a list exit*/
	if (!PyList_Check(p))
		return;

	len = PyList_Size(p);
	fprintf(stdout, "[*] Size of the Python list = %ld\n", len);
	fprintf(stdout, "[*] Allocated = \n");

	for (idx = 0; idx < len; idx++)
	{
		item = PyList_GetItem(p, idx);

		fprintf(stdout, "Element %ld: ", idx);
		print_type_str(item);
	}
}
