#define PY_SSIZE_T_CLEAN
#include <Python.h>

void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", Py_SIZE(list));
    printf("[*] Allocated = %ld\n", list->allocated);

    for (Py_ssize_t i = 0; i < Py_SIZE(list); i++)
    {
        PyObject *item = list->ob_item[i];
        const char *item_type = Py_TYPE(item)->tp_name;
        printf("Element %ld: %s\n", i, item_type);
    }
}

void print_python_bytes(PyObject *p)
{
    if (!PyBytes_Check(p))
    {
        printf("[.] bytes object info\n");
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    PyBytesObject *bytes = (PyBytesObject *)p;

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", Py_SIZE(bytes));

    // Print a maximum of 10 bytes
    Py_ssize_t print_size = Py_SIZE(bytes);
    if (print_size > 10)
    {
        print_size = 10;
    }

    printf("  trying string: ");
    for (Py_ssize_t i = 0; i < print_size; i++)
    {
        printf("%02x ", bytes->ob_sval[i] & 0xff);
    }
    printf("\n");
}
