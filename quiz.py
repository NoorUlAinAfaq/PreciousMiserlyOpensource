Quiz = [
  {
    "Question": "What is the capital of Pakistan?",
    "Options":["Karachi", "Islamabad", "Lahore", "Peshawar"],
    "Correct Answer": "B"
  },
  {
    "Question": "What is the capital of India?",
    "Options":["Bombay", "Delhi", "Agra", "Luckhnow"],
    "Correct Answer": "B"
    
  }
]
score = 0
# Accessing a question
for item in Quiz:
    print(item["Question"])
    for idx, option in enumerate(item['Options']):
      print(f"{idx}. {option}")
    user_answer = input("Enter your answer (A, B, C, or D): ")
    if user_answer.upper() == item["Correct Answer"]:
      print("Correct!")
      score = score + 1
    else:
      print("Wrong")

print(f"Your score is {score}")

