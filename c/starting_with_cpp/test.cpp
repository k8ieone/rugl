#include <iostream>

int main()
{
    std::cout << "Hello World!\n";
    int x;
    int width{5};
    std::cout << width << std::endl;
    width = 1;
    std::cout << width << "\n";
    std::cin >> x;
    std::cout << x << "\n";
    return 0;
}