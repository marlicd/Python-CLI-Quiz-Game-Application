# Python Program for a CLI Quiz Game

import random

print("Welcome to Marlic's general question quiz!!!")
print("Try your best to answer the following 20 questions correctly")
print("GOOD LUCK")

# Create list of 20 questions
Questions = [

    {
        "question": "What is the capital of Kenya?",
        "A": "Nairobi",
        "B": "Kampala",
        "C": "Dodoma",
        "D": "Kigali",
        "answer": "A"
    },

    {
        "question": "How many Counties are in Kenya",
        "A": "27",
        "B": "55",
        "C": "12",
        "D": "47",
        "answer": "D"
    },

    {
        "question": "How many arms of Government are there in Kenya?",
        "A": "5",
        "B": "12",
        "C": "3",
        "D": "1",
        "answer": "C"
    },

    {
        "question": "How many presidents has the Republic of Kenya had?",
        "A": "5",
        "B": "12",
        "C": "3",
        "D": "1",
        "answer": "A"
    },

    {
        "question": "Which is the Largest lake in Kenya",
        "A": "Lake Turkana",
        "B": "Lake Victoria",
        "C": "Lake Bogoria",
        "D": "Lake Nakuru",
        "answer": "A"
    },

    {
        "question": "How many countries are there in Africa?",
        "A": "47",
        "B": "102",
        "C": "55",
        "D": "77",
        "answer": "C"
    },

    {
        "question": "Which is the longest river in Africa?",
        "A": "River Zambizi",
        "B": "River Athi",
        "C": "River Victoria",
        "D": "River Nile",
        "answer": "D"
    },

    {
        "question": "How many Oceans surround Africa?",
        "A": "2",
        "B": "5",
        "C": "3",
        "D": "1",
        "answer": "A"
    },

    {
        "question": "What is the largest country in Africa?",
        "A": "Sudan",
        "B": "Algeria",
        "C": "Somalia",
        "D": "Nigeria",
        "answer": "B"
    },

    {
        "question": "How many continents are there in the world?",
        "A": "5",
        "B": "7",
        "C": "3",
        "D": "1",
        "answer": "B"
    },

    {
        "question": "Which is the biggest continent in the world?",
        "A": "Africa",
        "B": "Asia",
        "C": "USA",
        "D": "Europe",
        "answer": "B"
    },

    {
        "question": "Which is the most populated continent in the World?",
        "A": "Asia",
        "B": "Africa",
        "C": "Europe",
        "D": "Australia",
        "answer": "A"
    },

    {
        "question": "What is the capital of the United States of America?",
        "A": "New York",
        "B": "Los Angeles",
        "C": "Los Vegas",
        "D": "Washington DC",
        "answer": "D"
    },

    {
        "question": "Which is the strongest currency in the world?",
        "A": "Kuwait Dinar",
        "B": "United Sates Dollar",
        "C": "Euro",
        "D": "Pound",
        "answer": "A"
    },

    {
        "question": "What is the capital of Germany",
        "A": "Luxembourg",
        "B": "Berlin",
        "C": "Moscow",
        "D": "Helsinki",
        "answer": "B"
    },

    {
        "question": "How many bones does a Grown human have",
        "A": "207",
        "B": "120",
        "C": "206",
        "D": "126",
        "answer": "C"
    },

    {
        "question": "Which is the tallest mammal in the world?",
        "A": "Elephant",
        "B": "Blue Whale",
        "C": "Tiger",
        "D": "Giraffe",
        "answer": "D"
    },

    {
        "question": "Which is the largest body part in the human body?",
        "A": "Liver",
        "B": "Stomach",
        "C": "Brain",
        "D": "Heart",
        "answer": "A"
    },

    {
        "question": "Which body part contains the most fat?",
        "A": "Liver",
        "B": "Stomach",
        "C": "Heart",
        "D": "Brain",
        "answer": "D"
    },

    {
        "question": "Which number equates to pi?",
        "A": "3.142",
        "B": "67",
        "C": "1263",
        "D": "300000",
        "answer": "A"
    },

]

# Shuffle question order to generate a random question in sequence
random.shuffle(Questions)

# Set score to enable grading
Score = 0

# Loop through questions 
for item in Questions:

    print("\n" + item["question"])
    print("A.", item["A"])
    print("B.", item["B"])
    print("C.", item["C"])
    print("D.", item["D"])

    Answer = input("Enter answer (A/B/C/D): ")
    Answer = Answer.upper() # Convert the entered input into an uppercase letter

    # Check if answer is correct
    if Answer == item["answer"]:
        print("Correct")
        Score = Score + 1

    # Check for invalid input entered by the user
    elif Answer != "A" and Answer != "B" and Answer != "C" and Answer != "D":
        print("Invalid input")

    # If answer is wrong
    else:
        print("Wrong")
        print(f"Correct answer is {item['answer']}")

# Display score of the user after the test
print(f"\nYour Total Score is {Score} out of {len(Questions)}")


# Feedback for the 20 questions
if Score >= 17:
    print("Excellent")

elif Score >= 12:
    print("Good")

elif SCore >= 10:
    print(Fair)

else:
    print("Try Again")