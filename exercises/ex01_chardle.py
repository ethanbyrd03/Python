""""Exercise 1 Wordle recreation"""
__author__ = "730481841"

word_of_the_day: str = input("Enter a 5-character word: ")
if len(word_of_the_day) < 5:
    print("Error: Word must contain 5 characters")
    exit()
if len(word_of_the_day) > 5:
    print("Error: Word must contain 5 characters")
    exit()
character_guess: str = input("Enter a single character: ")
if len(character_guess) != 1:
    print("Error: Character must be a single character")
    exit()
number_correct: int = 0
print("Searching for " + character_guess + " in " + word_of_the_day)

if character_guess == word_of_the_day[0]:
    print(character_guess + " found at index 0")
    number_correct = number_correct + 1
if character_guess == word_of_the_day[1]:
    print(character_guess + " found at index 1")
    number_correct = number_correct + 1
if character_guess == word_of_the_day[2]:
    print(character_guess + " found at index 2")
    number_correct = number_correct + 1 
if character_guess == word_of_the_day[3]:
    print(character_guess + " found at index 3")
    number_correct = number_correct + 1
if character_guess == word_of_the_day[4]:
    print(character_guess + " found at index 4")
    number_correct = number_correct + 1
if number_correct == 0:
    print("No instances of " + character_guess + " found in " + word_of_the_day)
else:
    print(str(number_correct) + " instances of " + character_guess + " found in " + word_of_the_day)
