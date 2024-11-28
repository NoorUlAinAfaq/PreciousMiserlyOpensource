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
    print("\n".join(item["Options"])) 
    user_answer = input("Enter your answer (A, B, C, or D): ")
    if user_answer.upper() == item["Correct Answer"]:
      print("Correct!")
      score = score + 1
    else:
      print("Wrong")

print(f"Your score is {score}")

