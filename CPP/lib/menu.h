#include <iostream>

int menu() {
  std::cout << "                     --- Welcome to the Math Tools menu ---\n\
    \n\
    Tools:\n\
        1. Prime number checker\n\
    \n\
    Games:\n\
        2. Guess the number\n\
    \n\
    Notes:\n\
        Select a tool or game by entering the corresponding number.\n\
        To exit the program, enter 0.\n\n";
  int choice;
  std::cout << "Enter your choice: ";
  std::cin >> choice;
  return choice;
}