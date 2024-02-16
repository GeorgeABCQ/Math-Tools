#include <chrono>
#include <iostream>
#include <list>
#include <string>
#include <thread>

int randnum() {
  int low;
  int high;
  int times;
  int multiple = 0;
  std::list<int> list_num = {};
  std::cout << "Enter the lowest number the random number can be: ";
  std::cin >> low;
  std::cout << "Enter the highest number the random number can be: ";
  std::cin >> high;
  if (low > high || low == high) {
    std::cout << "Invalid range.\n";
    std::cout << "Press enter to return to the main menu ... ";
    std::cin.ignore(2);
    return -2;
  }
  // print message
  std::cout
      << "Do you want a random number to generate multiple times? (type 1 for "
         "yes, type "
         "anything else for no) ";
  std::cin >> multiple;

  std::cout << "Enter the number of random numbers you want: ";
  std::cin >> times;
  if (multiple != 1 && times > high - low + 1) {
    std::cout << "Invalid number of random numbers.\n";
    std::cout << "Press enter to return to the main menu ... ";
    std::cin.ignore(2);
    return -2;
  }
  if (times != 1) {
    std::cout << "The random numbers are: ";
  } else if (times == 1) {
    std::cout << "The random number is: ";
  } else if (times < 1) {
    std::cout << "Invalid number of random numbers.\n";
    std::cout << "Press enter to return to the main menu ... ";
    std::cin.ignore(2);
    return -2;
  }
  for (int i = 0; i < times; i++) {
    int num = rand() % high + low;
    if (multiple != 1 &&
        std::find(list_num.begin(), list_num.end(), num) != list_num.end()) {
      i--;
    } else {
      list_num.push_back(num);
      if (i == times - 1) {
        std::cout << num << ".\n";
      } else {
        std::cout << num << ", ";
      }
    }
  }
  std::cout << "Press enter to return to the main menu ... ";
  std::cin.ignore(2);
  return 0;
}
