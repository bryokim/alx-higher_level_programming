#include <Python.h>
#include <object.h>
#include <listobject.h>


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

	obj = (PyListObject *)p;
	len = PyList_Size(p);

	printf("[*] Size of the Python list = %ld\n", len);
	printf("[*] Allocated = %ld\n", obj->allocated);

	for (idx = 0; idx < len; idx++)
	{
		item = PyList_GetItem(p, idx);
		printf("Element %ld: %s\n", idx, Py_TYPE(item)->tp_name);
	}
}
