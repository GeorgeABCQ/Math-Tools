#include <iostream>
using namespace std;

// Function to calculate the highest common factor of two numbers

int hcf(int dev, int num1, int num2) {
  if (dev != 1) {
    cout << "Enter the first number: ";
    cin >> num1;
    cout << "Enter the second number: ";
    cin >> num2;
  }
  int hcf;
  int min = (num1 < num2) ? num1 : num2;
  for (int i = 1; i <= min; i++) {
    if (num1 % i == 0 && num2 % i == 0) {
      hcf = i;
    }
  }
  if (dev != 1) {
    cout << "The highest common factor of " << num1 << " and " << num2 << " is "
         << hcf << endl;
    cout << "Press enter to return to the main menu ... ";
    cin.ignore(2);
  }
  return hcf;
}
