#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic information about a Python list
 * @p: The PyObject representing a Python list
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
{
printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
}
}

/**
 * print_python_bytes - Prints basic information about a Python bytes object
 * @p: The PyObject representing a Python bytes object
 */

void print_python_bytes(PyObject *p)
{
PyBytesObject *bytes = (PyBytesObject *)p;
Py_ssize_t size;
Py_ssize_t i;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}
size = PyBytes_Size(p);
printf("  size: %ld\n", size);
printf("  trying string: %s\n", PyBytes_AS_STRING(p));
if (size < 10)
printf("  first %ld bytes:", size + 1);
else
printf("  first 10 bytes:");
for (i = 0; i < size + 1 && i < 10; i++)
{
printf(" %02x", bytes->ob_sval[i] & 0xff);
}
printf("\n");
}
