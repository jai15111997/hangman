# Project Title: Hangman

## A description of the project:

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.
This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.  project, and what you learned

## Installation instructions:

Signup and create GitHub account and install VS-Code. Alternatively, use the Git-Bash/ Zsh/ Powershell terminal to execute commands.
Copy the share code URL from the gitHub repository and clone it in the local machine using the command "git clone (URL)". Execute milestone_5.py from the terminal to run the game.

## Usage instructions:

- ask_for_input(): Asks for input of a single alphabet character until proper input is achieved. Displays appropriate message in case of invalid input. Displays a warning message when entering previous characters again. Calls check_guess function.

- check_guess(): Converts the user input into a lowercase character and checks if it falls inside the computer's generated word. It displays appropriate message depending on the outcome. It also captures all instances of that character in the guessed word.

- playgame(): Helps in determining the output of the game based on remaining number lives and letters to be guessed. Calls the ask_for_input until the player lose/wins.

## File structure of the project:

- README.md: ReadME file giving the overview of the project's code and methods.

- milestone_2.py: Initial Concept of working with limited inputs.

- milestone_3.py: An improved version of milestone_2.py having adequate functions and improved readability 

- milestone_4.py: Integrated the previous code into class environment and the functions are now called by means of an instance of class.

- milestone_5.py: Final complete code from milestone_4.py that determines the outcome of the game. Run this to play the game!

## License information:

MIT License

Copyright (c) [2023] [AiCore]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

