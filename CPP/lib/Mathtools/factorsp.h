#include <iostream>
#include <list>

using namespace std;

list<int> factorsp(int dev, int num) {
  list<int> factorsp = {};
  if (dev != 1) {
    cout << "Type the number you want to decompose to prime numbers: ";
    cin >> num;
  }
  int i = 2;
  if (dev != 1) {
    cout << "The prime factors of " << num << " are: ";
  }
  while (num > 1) {
    if (num % i == 0) {
      num /= i;
      if (dev != 1) {
        if (num != 1) {
          cout << i << ", ";
        } else {
          cout << i << endl;
        }
      } else {
        factorsp.push_back(i);
      }
      i = 2;
    } else {
      i++;
    }
  }
  if (dev == 1) {
    return factorsp;
  } else {
    cout << "Press enter to return to the main menu ... ";
    cin.ignore(2);
    return factorsp;
  }
  return {-69};
}