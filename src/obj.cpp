#include "obj.h"

int add(int i, int j) {
    return i + j;
}

int multiply(int i, int j) {
    return i * j;
}

int shift(int x, int shift) {
    return x << shift;
}


my_obj::my_obj(int x, int y) {
    this->x = x;
    this->y = y;
}

int my_obj::func() {
    return this->x * (this->y + 1) * (this->x - this->y);
}
