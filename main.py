# # import time

# # # timestamp = time.strftime("%H:%M:%S")
# # print(time.clock_gettime(9))
# # print(time.strftime("%H:%M:%S"))

# quiz = [
#   {
#       "question": "What is the capital of France?",
#       "options": ["A) Paris", "B) Madrid", "C) Berlin", "D) Rome"],
#       "correct_answer": "A",
#   },
#   {
#       "question": "What is 2 + 2?",
#       "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
#       "correct_answer": "B",
#   },
# ]

# # Accessing a question
# for item in quiz:
#   print(item["question"])
#   print("\n".join(item["options"])) 
#   user_answer = input("Enter your answer (A, B, C, or D): ")

#   if user_answer.upper() == item["correct_answer"]:
#     print("Correct!")
#   else:
#     print("Wrong")
#     print("\n Correct answer is:" + item["correct_answer"])

# name = "bob"
# print(f"Hello, {name.upper()}!")

# name = "Alice"
# age = 25
# bio = f"""
# Name: {name}
# Age: {age}
# """
# print(bio)

# x = 42
# print(f"x = {x}")            
# print(f"{x = }")        

def fibonacci(n):
  if n == 0:  # Base case
      return 0
  elif n == 1:  # Base case
      return 1
  else:
      return fibonacci(n - 1) + fibonacci(n - 2)
  


print(fibonacci(5))  

