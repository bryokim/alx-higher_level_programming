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
	long int idx, len;
	PyListObject *obj;

	obj = (PyListObject *)p;
	len = PyList_Size(p);

	printf("[*] Size of the Python list = %ld\n", len);
	printf("[*] Allocated = %ld\n", obj->allocated);

	for (idx = 0; idx < len; idx++)
		printf("Element %ld: %s\n", idx, Py_TYPE(obj->ob_item[idx])->tp_name);
}
