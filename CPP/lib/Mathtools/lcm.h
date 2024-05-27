// Lowest common multiple function
#include <iostream>

using namespace std;

int main(int dev, int num1, int num2) {
  int lcm;
  if (dev != 1) {
    cout << "Enter the first number: ";
    cin >> num1;
    cout << "Enter the second number: ";
    cin >> num2;
  }
  int max;
  if (num1 > num2) {
    max = num1;
  } else {
    max = num2;
  }
  while (true) {
    if (max % num1 == 0 && max % num2 == 0) {
      lcm = max;
      break;
    }
    max++;
  }
  if (dev != 1) {
    cout << "The lowest common multiple of " << num1 << " and " << num2
         << " is " << lcm << endl;
    cout << "Press enter to return to the main menu ... ";
    cin.ignore(2);
  }
  return lcm;
}
