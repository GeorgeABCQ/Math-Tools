#include <iostream>
#include <list>

using namespace std;

list<int> factors(int dev, int num) {
  list<int> factors = {};
  if (dev != 1) {
    cout << "Enter the number you want to find the factors of: ";
    cin >> num;
  }
  for (int trynum = 1; trynum <= num; trynum++) {
    if (num % trynum == 0) {
      if (dev != 1) {
        if (trynum != num) {
          cout << trynum << ", ";
        } else {
          cout << trynum << endl;
        }
      } else {
        factors.push_back(trynum);
        cout << trynum << endl;
      }
    }
  }
  return factors;
}