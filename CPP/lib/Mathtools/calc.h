#include <cmath>
#include <iostream>
using namespace std;

double add(double num1, double num2) {
  double ans = num1 + num2;
  return ans;
}

double sub(double num1, double num2) {
  double ans = num1 - num2;
  return ans;
}

double mul(double num1, double num2) {
  double ans = num1 - num2;
  return ans;
}

double div(double num1, double num2) {
  if (num2 == 0) {
    std::cout << "Error: Cannot divide by zero.\n";
    return NAN;
  }
  double ans = num1 / num2;
  return ans;
}

double pow(double num1, int num2) {
  double ans = 1;
  for (int times = 0; times < num2; times++) {
    ans = ans * num1;
  }
  return ans;
}

double sqrt(double num1) {
  double ans = sqrt(num1);
  return ans;
}

int mod(int num1, int num2) {
  int ans = num1 % num2;
  return ans;
}

int calc() {
  std::cout << "Welcome to the basic calculator!\n\
    Type add to add two numbers.\n\
    Type sub to subtract two numbers.\n\
    Type mul to multiply two numbers.\n\
    Type div to divide two numbers.\n\
    Type pow to raise a number to a power.\n\
    Type sqrt to find the square root of a number.\n\
    Type mod to find the remainder of a number.\n\
    Type quit to exit the calculator.\n\
    Type ans to see the last answer.\n";
  std::cout << "Enter a command: ";
  std::string command;
  std::cin >> command;
  double ans = NAN;
  if (command == "add") {
    double num1, num2;
    std::cout << "Enter the first number: ";
    std::cin >> num1;
    std::cout << "Enter the second number: ";
    std::cin >> num2;
    double ans = add(num1, num2);
    std::cout << "The answer is: " << ans << "\n";
  } else if (command == "sub") {
    double num1, num2;
    std::cout << "Enter the first number: ";
    std::cin >> num1;
    std::cout << "Enter the second number: ";
    std::cin >> num2;
    double ans = sub(num1, num2);
    std::cout << "The answer is: " << ans << "\n";
  } else if (command == "mul") {
    double num1, num2;
    std::cout << "Enter the first number: ";
    std::cin >> num1;
    std::cout << "Enter the second number: ";
    std::cin >> num2;
    double ans = mul(num1, num2);
    std::cout << "The answer is: " << ans << "\n";
  } else if (command == "div") {
    double num1, num2;
    std::cout << "Enter the first number: ";
    std::cin >> num1;
    std::cout << "Enter the second number: ";
    std::cin >> num2;
    double ans = div(num1, num2);
    std::cout << "The answer is: " << ans << "\n";
  } else if (command == "pow") {
    double num1;
    int num2;
    std::cout << "Enter the number: ";
    std::cin >> num1;
    std::cout << "Enter the power: ";
    std::cin >> num2;
    double ans = pow(num1, num2);
    std::cout << "The answer is: " << ans << "\n";
  } else if (command == "sqrt") {
    double num1;
    std::cout << "Enter the number: ";
    std::cin >> num1;
    double ans = sqrt(num1);
    std::cout << "The answer is: " << ans << "\n";
  } else if (command == "mod") {
    int num1, num2;
    std::cout << "Enter the first number: ";
    std::cin >> num1;
    std::cout << "Enter the second number: ";
    std::cin >> num2;
    int ans = mod(num1, num2);
    std::cout << "The answer is: " << ans << "\n";
  } else if (command == "quit") {
    return 0;
  } else if (command == "ans") {
    std::cout << "The answer is: " << ans << "\n";
  } else {
    std::cout << "Invalid command. Please try again.\n";
  }
}