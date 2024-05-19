#include <iostream>
#include <list>
using namespace std;

// Function to decompose a number into prime factors

std::list<int> dpf(int num, int dev, list<int> factors = {}) {
  if (dev != 1) {
    std::cout << "Type the number you want to decompose to prime numbers: ";
    std::cin >> num;
  }
  int i = 2;
  if (dev != 1) {
    std::cout << "The prime factors of " << num << " are: ";
  }
  while (num > 1) {
    if (num % i == 0) {
      num /= i;
      if (dev != 1) {
        if (num != 1) {
          std::cout << i << ", ";
        } else {
          std::cout << i << std::endl;
        }
      } else {
        factors.push_back(i);
      }
      i = 2;
    } else {
      i++;
    }
  }
  if (dev == 1) {
    return factors;
  } else {
    std::cout << "Press enter to return to the main menu ... ";
    std::cin.ignore(2);
    return {0};
  }
  return {0};
}
