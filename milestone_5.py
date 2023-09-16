import random
class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for x in range(len(self.word))]
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for count in range(len(self.word)):
                if self.word[count] == guess:
                    self.word_guessed[count] = guess
                    self.num_letters -= 1
            self.list_of_guesses.append(guess)
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")
            self.list_of_guesses.append(guess)
    def ask_for_input(self):
        guess = ''
        while True:
            guess = input("Enter a single letter\n")
            if len(guess) != 1 or guess.isalpha() == False:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                print(self.word_guessed)
    def playgame(self):
        while True:
            if self.num_lives == 0:
                print('You lost!')
                break
            elif self.num_letters <= 0:
                print('Congratulations. You won the game!')
                break
            self.ask_for_input()
word_list = ["apple", "banana", "cherry", "date", "elderberry"]
num_lives = 5
game = Hangman(word_list, num_lives)
game.playgame()