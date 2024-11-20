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

def fibonacci_iterative(n):
    """Prints the first n Fibonacci numbers using an iterative approach."""
    # Handle edge cases
    if n <= 0:
        print("Please enter a positive integer.")
        return

    # Base cases
    if n == 1:
        print("0")
        return
    elif n == 2:
        print("0, 1")
        return

    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    print(a,"\n",b)

    # Generate the rest of the Fibonacci sequence
    for _ in range(n - 2):
        c = a + b
        print(c)
        a, b = b, c

# Example usage
fibonacci_iterative(7)
