#include <iostream>

int menu() {
  std::cout << "                     --- Welcome to the Math Tools menu ---\n\
    \n\
    Tools:\n\
        1. Prime number checker\n\
        2. Random number generator\n\
        3. Decompose a number into prime factors\n\
        4. Calculate the highest common factor of two numbers\n\
        5. Calculate the lowest common multiple of two numbers\n\
        6. Find the prime factors of a number\n\
        7. Find the factors of a number\n\
        8. Co-prime number checker\n\
        9. Basic calculator.\n\
    \n\
    Games:\n\
        10. Guess the number\n\
        11. Rock, Paper, Scissors\n\
    \n\
    Notes:\n\
        Select a tool or game by entering the corresponding number.\n\
        To exit the program, enter 0.\n\n";
  int choice;
  std::cout << "Enter your choice: ";
  std::cin >> choice;
  return choice;
}
