#include <pybind11/pybind11.h>
#include "obj.h"

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)


namespace py = pybind11;

PYBIND11_MODULE(_core, m) {
    m.doc() = R"pbdoc(
        Pybind11 example plugin
        -----------------------

        .. currentmodule:: seminar_hacivutzim

        .. autosummary::
           :toctree: _generate

           add
           subtract
    )pbdoc";

    m.def("add", &add, R"pbdoc(
        Add two numbers

        Some other explanation about the add function.
    )pbdoc");

    m.def("subtract", [](int i, int j) { return i - j; }, R"pbdoc(
        Subtract two numbers

        Some other explanation about the subtract function.
    )pbdoc");

    m.def("multiply", &multiply, py::arg("x"), py::arg("y"), R"pbdoc(
        abc
    )pbdoc");

    m.def("shift", &shift, py::arg("x"), py::arg("shift"), R"pbdoc(
        this is the documentation of shift.
    )pbdoc");

    py::class_<my_obj>(m, "py_obj")
        .def(py::init<int, int>())
        .def("func", &my_obj::func);

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}
