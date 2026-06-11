#!/usr/bin/env python3
import os
class Question:
    def __init__(self, text, option_a, option_b, option_c, correct_answer):
        self.text = text
        self.option_a = option_a
        self.option_b = option_b
        self.option_c = option_c
        self.correct_answer = correct_answer.strip().lower()

    def display(self):
        print(f"\n{self.text}")
        print(f"a) {self.option_a}")
        print(f"b) {self.option_b}")
        print(f"c) {self.option_c}")

class QuizGame:
    def __init__(self, filename):
        self.filename = filename
        self.questions = []
        self.score = 0
        
        #load questions here instead!!!

    def load_questions(self):
        if not os.path.exists(self.filename):
            print(f"Error: File '{self.filename}' not found!")
            return False
        with open(self.filename, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split('|')
                if len(parts) == 5:
                    text, a, b, c, correct = parts
                    q = Question(text, a, b, c, correct)
                    self.questions.append(q)
        return True

    def play(self):
        if not self.questions:
            print("No questions loaded. Game over")
            return
        print("=== Welcome to the quiz game! ===")
        for q in self.questions:
            q.display()
            user_answer = input("Your answer (a/b/c): ").strip().lower()
            if user_answer == q.correct_answer:
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong, the correct answer was: {q.correct_answer}")
        print("\n=== Game Over ===")
        print(f"Your final score: {self.score} out of {len(self.questions)}")

if __name__ == "__main__":
    #make new game object
	game = QuizGame("questions.txt")
    #call load questions, member function of game
	if game.load_questions():
        #now questions are loaded, game can be played
		game.play()
    #Ollie thinks this is stupid, because surely, you ALWAYS want to load the questions for your quiz....
    #So Ollie wants you to load the questions in the constructor of the quizgame class
