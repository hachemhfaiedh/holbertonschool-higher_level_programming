#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 *print_python_list_info - print python list info
 *@p: parameter
 *Return: Void
 */

void print_python_list_info(PyObject *p)
{
	PyObject *po;
	Py_ssize_t psize = 0, i, n;

        n = ((PyListObject *)p)->allocated;
       	psize = Py_SIZE(p);
	printf("[*] Size of the Python List = %zu\n", psize);
	printf("[*] Allocated = %zu\n", n);
	for (i = 0; i < psize; i++)
	{
		printf("Element %zu: ", i);
		po = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(po)->tp_name);
	}
}
