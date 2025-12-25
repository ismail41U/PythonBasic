
class Questions:
    def __init__(self, question_text, answer_choices, correct_answer,exam_score):
        self.question_text = question_text
        self.answer_choices = answer_choices
        self.correct_answer = correct_answer
        self.exam_score = exam_score

    def display_question(self):
        print(self.question_text)
        for idx, choice in enumerate(self.answer_choices, start=1):
            print(f"{idx}. {choice}")

    def check_answer(self, user_answer):
        # Convert user input to integer and compare with correct answer
        try:
            choice_index = int(user_answer)
            if 1 <= choice_index <= len(self.answer_choices):
                return self.answer_choices[choice_index - 1] == self.correct_answer
            return False
        except ValueError:
            return False
    
    def get_score(self):
        return self.exam_score
    

q1 = Questions("What is the capital of France?", 
               ["Berlin", "Madrid", "Paris", "Rome"], 
               "Paris", 33)
q2 = Questions("Which planet is known as the Red Planet?",  
               ["Earth", "Mars", "Jupiter", "Saturn"], 
               "Mars", 33)
q3 = Questions("What is the largest ocean on Earth?", 
               ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "Pacific Ocean", 36)


questions_list = [q1, q2, q3]
total_score = 0
max_score = sum(q.get_score() for q in questions_list)

for i, question in enumerate(questions_list, start=1):
    print(f"\n=== Question {i} ===")
    question.display_question()
    user_answer = input("Answer (1-4): ")
    
    if question.check_answer(user_answer):
        print("✓ Correct !")
        total_score += question.get_score()
    else:
        print(f"✗ wrong answer! correct answer : {question.correct_answer}")

print(f"\n=== Conclusion ===")
print(f"Total Score: {total_score}/{max_score}")
percentage = (total_score / max_score) * 100
print(f"Success Percentage : % {percentage:.1f}")