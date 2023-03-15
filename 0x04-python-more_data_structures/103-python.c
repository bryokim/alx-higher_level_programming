#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * print_python_bytes - prints basic info about Python bytes objects.
 *
 * @p: pointer to a Python object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, idx, allowed_bytes;
	PyBytesObject *bytes;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);
	bytes = (PyBytesObject *)p;
	allowed_bytes = size >= 10 ? 9 : size;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %ld bytes: ", allowed_bytes + 1);

	for (idx = 0; idx <= allowed_bytes; idx++)
	{
		if (idx < allowed_bytes)
			printf("%02x ", bytes->ob_sval[idx]);
		else
			printf("%02x\n", bytes->ob_sval[idx]);
	}
}

/**
 * print_python_list - print basic info about Python lists.
 *
 * @p: Pointer to a Python object struct.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t idx;
	PyObject *item;
	Py_ssize_t size = PyList_Size(p);
	PyListObject *list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (idx = 0; idx < size; idx++)
	{
		item = list->ob_item[idx];
		printf("Element %ld: %s\n", idx, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
