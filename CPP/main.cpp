#include <iostream>
#include <string>

#include "lib\Games\guessnum.h"
#include "lib\Mathtools\isprime.h"
#include "lib\menu.h"

using namespace std;

int main() {
  int choice = -1;
  while (choice != 0) {
    int num1;
    choice = menu();
    if (choice == 1) {
      isprime(0, 0);
    } else if (choice == 2) {
      guessnum();
    } else if (choice == 0) {
      cout << "Goodbye!";
      _sleep(1000);
    } else {
      cout << "Invalid choice. Please try again.\n";
      _sleep(1000);
    }
    std::cout << "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n";
  }
  return 0;
}