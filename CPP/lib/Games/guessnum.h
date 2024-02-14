#include <iostream>

int guessnum() {
  int big;
  int trytop;
  int exit = 1;
  std::cout << "Welcome to the Guess the Number game!\n";
  while (exit != 0) {
    int tries = 1;
    std::cout
        << "What's the highest number you'd like to guess? (default is 100): ";
    std::cin >> big;
    std::cout << "How many tries would you like to have? (0 for unlimited, "
                 "default is 20): ";
    std::cin >> trytop;
    if (trytop == 0) {
      trytop = -1;
    } else if (trytop < 0) {
      trytop = 20;
    }

    if (big < 2) {
      big = 100;
    }

    int num = rand() % big + 1;
    int guess = -1;
    while (guess != num && (tries - 1 < trytop || trytop == -1)) {
      if (trytop == -1) {
        std::cout << "Guess " << tries
                  << " out of unlimited guesses. Guess the number: ";
      } else {
        std::cout << "Guess " << tries << " out of " << trytop
                  << ". Guess the number: ";
      }
      std::cin >> guess;
      if (guess > num) {
        std::cout << "Too high!\n";
      } else if (guess < num) {
        std::cout << "Too low!\n";
      } else if (guess == num) {
        std::cout << "Congratulations! The number is " << num
                  << ". You guessed the number in " << tries << " tries.\n";
        break;
      }
      tries++;
    }
    if (tries - 1 == trytop) {
      std::cout << "You lose! The number is " << num
                << ". Better luck next time!\n";
    }
    std::cout
        << "Would you like to play again? (type 1 for yes, type any NUMBER "
           "for no) ";
    std::cin >> exit;
    if (exit != 1) {
      exit = 0;
    }
  }
  return 0;
}