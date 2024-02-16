#include <iostream>

// Function to check if a number is prime
// if dev == 1 than it will not require user input
// returning 0 means the number is not prime, 1 means it is prime, 2 means it is
// 1, -1 means it cannot be difined
int isprime(int dev, int num) {
  char nothing;
  if (dev != 1) {
    std::cout << "Enter a number : ";
    std::cin >> num;
  }
  if (num == 1) {
    if (dev != 1) {
      std::cout << "1 is not a prime number nor a composite number."
                << std::endl;
      std::cout << "Press enter to return to the main menu ... ";
      std::cin.ignore(2);
    }
    return 2;
  } else {
    if (num < 1) {
      if (dev != 1) {
        std::cout
            << num
            << " cannot be defined as a prime number nor a composite number."
            << std::endl;
        std::cout << "Press enter to return to the main menu ... ";
        std::cin.ignore(2);
      }
      return -1;
    } else {
      for (int i = 2; i < num; i++) {
        if (num % i == 0) {
          if (dev != 1) {
            std::cout << num << " is not a prime number." << std::endl;
            std::cout << "Press enter to return to the main menu ... ";
            std::cin.ignore(2);
          }
          return 0;
        }
      }
      if (dev != 1) {
        std::cout << num << " is a prime number." << std::endl;
        std::cout << "Press enter to return to the main menu ... ";
        std::cin.ignore(2);
      }
      return 1;
    }
  }
  return -2;
}
