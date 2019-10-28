#include <iostream>

int multiply_two_numbers(int n1, int n2){
    int result;
    result = n1 * n2;
    return result;
}

int add_two_numbers(int n1, int n2){
    int result;
    result = n1 + n2;
    return result;
}

int subtract_two_numbers(int n1, int n2){
    int result;
    result = n1 - n2;
    return result;
}

float divide_two_numbers(float n1, float n2){
    float result;
    result = n1 / n2;
    return result;
}

int get_double(int n1){
    return n1 * n1;
}

int main(){
    std::cout << "2 times 2 is " << multiply_two_numbers(2, 2) << "\n";
    std::cout << "2 plus 2 is " << add_two_numbers(2, 2) << "\n";
    std::cout << "2 minus 2 is " << subtract_two_numbers(2, 2) << "\n";
    std::cout << "60 divided by 7 is " << divide_two_numbers(60, 7) << "\n";
    return 0;
}
