#include <iostream>
#include <list>
#include <string>

int rps() {
  std::string choice;
  int choice2;
  int compchoice;
  int result;
  int score = 0;
  int count = 1;
  int nocount = 0;
  bool exit = false;
  std::cout << "Welcome to Rock, Paper, Scissors!\n";
  while (exit == false) {
    std::cout
        << "Type 'r' for rock, 'p' for paper, 's' for scissors, 'exit' for "
           "exit.\n";
    std::cout << "Round " << count << ". Your score is " << score
              << ". Enter your choice: ";
    std::cin >> choice;
    compchoice = rand() % 3 + 1;
    if (choice == "r" || choice == "rock") {
      choice2 = 1;
    } else if (choice == "p" || choice == "paper") {
      choice2 = 2;
    } else if (choice == "s" || choice == "scissor" || choice == "scissors") {
      choice2 = 3;
    } else if (choice == "exit") {
      std::cout << "Goodbye!\n";
      std::cout << "Press enter to return to the main menu ... ";
      std::cin.ignore(2);
      exit = true;
    } else {
      std::cout << "Invalid choice.\n";
      nocount = 1;
    }
    if (choice2 == compchoice) {
      result = 0;
    } else if (choice2 == 1 && compchoice == 3) {
      result = 1;
      score += 1;
    } else if (choice2 == 2 && compchoice == 1) {
      result = 1;
      score += 1;
    } else if (choice2 == 3 && compchoice == 2) {
      result = 1;
      score += 1;
    } else {
      result = 2;
      score -= 1;
    }
    if (compchoice == 1) {
      std::cout << "The computer chose rock.\n ";
    } else if (compchoice == 2) {
      std::cout << "The computer chose paper.\n ";
    } else {
      std::cout << "The computer chose scissors.\n ";
    }
    if (result == 0) {
      std::cout << "It's a tie!\n";
    } else if (result == 1) {
      std::cout << "You win! + 1 score.\n";
    } else {
      std::cout << "You lose! - 1 score.\n";
    }
    if (nocount == 0) {
      count += 1;
    } else {
      nocount = 0;
    }
    return 0;
  }
  return 1;
}
