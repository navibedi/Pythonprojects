question_list = ['Which planet is known as the "Red planet"?', "Who wrote the play 'Romeo and Juliet'?", "Which of these religious observances lasts for the shortest period of time during the calendar year?", "Which of these cetaceans is classified as a “toothed whale”?", " In 1718, which pirate died in battle off the coast of what is now North Carolina?"]
options_list = [["Jupiter", "Venus", "Mars", "Saturn"], ["William Shakespeare", "Jane Austen", "Charles Dickens", "Mark Twain"], ["Ramadan", "Diwali","Lent", "Hanukkah"], ["Minke whale", "Sperm whale", "Gray whale", "Humpback whale"], ["Luffy", "Bartholomew Roberts", "Captain Kidd", "Blackbeard"]]

# These variables are created to separate the nested lists in the "options_list"
answer_1 = options_list[0]
answer_2 = options_list[1]
answer_3 = options_list[2]
answer_4 = options_list[3]
answer_5 = options_list[4]

total_points = 100  # Initialize total points

# This is the function to display answers in option-like form:
def option_ans(r):
    options_string = ""
    for index, element in enumerate(r):
        option = chr(ord("a") + index)
        options_string += f"{option}) {element}\n"
    return options_string

#This function is used to match the correct answer with the question and also update the points system if the answer is correct
def correct_ans(user_input, correct_answer):
    global total_points  # Access the global variable

    if user_input in ["a", "b", "c", "d"] and user_input == correct_answer:
        total_points *= 10  # Increment by a factor of 10
        return f"Correct answer! You earned ${total_points}."
    else:
        return f"Incorrect answer, the right answer is {correct_answer}. Your points remain unchanged."

q1 = print("Q1) ", question_list[0])
print(option_ans(answer_1))
# User input for the first question
user_input = input("Please give the correct option: ").lower()  # Convert user input to lowercase
ans1 = correct_ans(user_input, "c")
print(ans1)
print(f"Total Points: ${total_points}\n")
print()

q2 = print("Q2) ", question_list[1])
print(option_ans(answer_2))
# User input for the second question
user_input = input("Please give the correct option: ").lower()  # Convert user input to lowercase
ans2 = correct_ans(user_input, "a")
print(ans2)
print(f"Total Points: ${total_points}\n")
print()

q3 = print("Q3) ", question_list[2])
print(option_ans(answer_3))
# User input for the third question
user_input = input("Please give the correct option: ").lower()  # Convert user input to lowercase
ans3 = correct_ans(user_input,"b")
print (ans3)
print(f"Total Points: ${total_points}\n")
print()

q4 = print("Q4) ", question_list[3])
print (option_ans(answer_4))
# User input for the third question
user_input = input("Please give the correct option: ").lower()  # Convert user input to lowercase
ans4 = correct_ans(user_input, "b")
print (ans4)
print(f"Total Points: ${total_points}\n")
print()

q5 = print("Q5) ", question_list[4])
print (option_ans(answer_5))
# User input for the third question
user_input = input("Please give the correct option: ").lower()  # Convert user input to lowercase
ans5 = correct_ans(user_input, "d")
print (ans5)
print(f"Congratulations, the total points you've earned are: ${total_points}")
print()
