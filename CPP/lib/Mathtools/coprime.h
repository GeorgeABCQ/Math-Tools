#include <iostream>

// Function to check if two numbers are coprime
int hcf_min(int num1, int num2) {
  int hcf;
  int min;
  if (num1 < num2) {
    min = num1;
  } else {
    min = num2;
  }
  for (int i = 1; i <= min; i++) {
    if (num1 % i == 0 && num2 % i == 0) {
      hcf = i;
    }
  }
  return hcf;
}

bool coprime(int dev, int num1, int num2) {
  if (dev != 1) {
    std::cout << "Enter the first number: ";
    std::cin >> num1;
    std::cout << "Enter the second number: ";
    std::cin >> num2;
  }
  int hcf_ans = hcf_min(num1, num2);
  if (hcf_ans == 1) {
    if (dev != 1) {
      std::cout << num1 << " and " << num2 << " are coprime.\n";
      std::cout << "Press enter to return to the main menu ... ";
      std::cin.ignore(2);
    }
    return true;
  } else {
    if (dev != 1) {
      std::cout << num1 << " and " << num2 << " are not coprime.\n";
      std::cout << "Press enter to return to the main menu ... ";
      std::cin.ignore(2);
    }
    return false;
  }
  return false;
}
