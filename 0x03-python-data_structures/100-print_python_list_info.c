#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>


/**
 * print_python_list_info - print info about a Python list.
 *
 * @p: PyObject representing a Python list.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t idx, len;
	PyObject *item;
	PyListObject *obj;

	/* If p is not a list or an instance of a list exit*/
	if (!PyList_Check(p))
		return;

	obj = (PyListObject *)p;
	len = PyList_Size(p);

	fprintf(stdout, "[*] Size of the Python list = %ld\n", len);
	fprintf(stdout, "[*] Allocated = %ld\n", obj->allocated);

	for (idx = 0; idx < len; idx++)
	{
		item = PyList_GetItem(p, idx);
		fprintf(stdout, "Element %ld: %s\n", idx, Py_TYPE(item)->tp_name);
	}
}
