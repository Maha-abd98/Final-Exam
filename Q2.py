class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def display_question(self):
        print(self.question)
        for index, option in enumerate(self.options, start=1):
            print(f"{index}. {option}")

    def check_answer(self, user_answer):
        return user_answer.lower() == self.correct_answer.lower()

questions = [
    Question("What is the capital of France?", ["London", "Berlin", "Paris", "Madrid"], "C"),
    Question("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Saturn"], "A"),
    Question("What is the largest mammal?", ["Elephant", "Blue whale", "Giraffe", "Hippopotamus"], "B"),
    Question("Who painted the Mona Lisa?", ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo"], "B"),
    Question("What's the largest ocean in the world?", ["Atlantic", "Indian", "Arctic", "Pacific"], "D"),
    Question("Which country is known as the Land of the Rising Sun?", ["China", "Korea", "Japan", "Vietnam"], "C"),
    Question("Which gas do plants absorb from the atmosphere?", ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"], "B"),
    Question("What is the primary ingredient of guacamole?", ["Tomato", "Avocado", "Onion", "Chili"], "B"),
    Question("Which mountain range is the longest in the world?", ["Andes", "Himalayas", "Rockies", "Alps"], "A"),
    Question("Who wrote 'Romeo and Juliet'?", ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"], "B")
]

def get_user_input():
    while True:
        user_input = input("Enter your answer (A, B, C, D): ").upper()
        if user_input in ['A', 'B', 'C', 'D']:
            return user_input
        else:
            print("Invalid input. Please enter A, B, C, or D.")

def play_game(player):
    score = 0
    for question in questions:
        print(f"\n{player}:")
        question.display_question()
        user_input = get_user_input()
        if question.check_answer(user_input):
            score += 1
    return score

def main():
    player1_score = play_game("Player 1")
    player2_score = play_game("Player 2")

    print("\nGame Over!")
    print(f"Player 1's score: {player1_score}")
    print(f"Player 2's score: {player2_score}")

    if player1_score > player2_score:
        print("Player 1 wins!")
    elif player2_score > player1_score:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
