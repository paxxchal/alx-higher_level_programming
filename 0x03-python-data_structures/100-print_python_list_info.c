#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: PyObject pointer representing the Python list
 */
void print_python_list_info(PyObject *p)
{
    int i;
    int size;
    int allocated;
    PyObject *item;

    size = Py_SIZE(p);
    allocated = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

int main(void)
{
    PyObject *l;
    l = Py_BuildValue("[s, s]", "hello", "World");

    print_python_list_info(l);

    PyList_SetItem(l, 1, NULL);
    print_python_list_info(l);

    l = PyList_Append(l, Py_BuildValue("i", 4));
    l = PyList_Append(l, Py_BuildValue("i", 5));
    l = PyList_Append(l, Py_BuildValue("d", 6.0));
    l = PyList_Append(l, Py_BuildValue("(ii)", 9, 8));
    l = PyList_Append(l, Py_BuildValue("[iii]", 9, 8, 1024));
    l = PyList_Append(l, Py_BuildValue("s", "My string"));

    print_python_list_info(l);

    l = PyList_GetSlice(l, 1, 3);
    print_python_list_info(l);

    Py_XDECREF(l);

    return (0);
}
