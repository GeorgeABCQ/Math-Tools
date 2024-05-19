#include <chrono>
#include <iostream>
#include <string>
#include <thread>

#include "lib\Games\guessnum.h"
#include "lib\Games\rps.h"
#include "lib\Mathtools\dpf.h"
#include "lib\Mathtools\hcf.h"
#include "lib\Mathtools\isprime.h"
#include "lib\Mathtools\randnum.h"
#include "lib\menu.h"

using namespace std;

int main() {
  int choice = -1;
  int error = 0;
  int num1;
  while (choice != 0) {
    choice = menu();
    if (choice == 1) {
      isprime(0, 0);
    } else if (choice == 2) {
      randnum();
    } else if (choice == 5) {
      guessnum();
    } else if (choice == 6) {
      rps();
    } else if (choice == 3) {
      dpf(0, 0);
    } else if (choice == 4) {
      hcf(0, 0, 0);
    } else if (choice == 0) {
      cout << "Goodbye!";
      std::this_thread::sleep_for(std::chrono::seconds(1));
    } else {
      error = 1;
    }
    std::cout << "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n";
    if (error == 1) {
      std::cout << "Invalid choice. Please try again.\n";
      error = 0;
    }
  }
  return 0;
}