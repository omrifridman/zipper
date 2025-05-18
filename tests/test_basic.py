from __future__ import annotations

import seminar_hacivutzim as m


def test_version():
    assert m.__version__ == "0.0.1"


def test_add():
    assert m.add(1, 2) == 3


def test_sub():
    assert m.subtract(1, 2) == -1


def main():
    test_add()
    test_sub()
    test_version()
    print(f"1 + 2 = {m.add(1, 2)}")
    print(f"5 - 2 = {m.subtract(5, 2)}")
    print(f"{m.multiply(1, 4) = }")
    print(f"{m.shift(5, 3) = }")

    obj = m.py_obj(3, 5)
    print(obj.func())


if __name__ == "__main__":
    main()
