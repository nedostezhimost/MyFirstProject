#run_from_me.py
import quiz

if __name__ == '__main__':
	game = quiz.QuizGame("questions.txt")
	game.play()
