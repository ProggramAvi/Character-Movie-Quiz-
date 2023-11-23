def gilmore_girls_quiz():
    print("Welcome to the Gilmore Girls Character Quiz!")
    print("Answer the following 10 questions to find out which character you are.\n")

    # Initialize a dictionary to store the scores for each character
    character_scores = {
        "Rory": 0,
        "Lorelai": 0,
        "Luke": 0,
        "Dean": 0,
        "Jess": 0,
        "Sookie": 0,
        "Jackson": 0,
        "Michelle": 0,
        "Max Medina": 0,
        "Lane": 0
    }

    # Questions and their corresponding characters' scores
    questions = [
        {"question": "Do you like coffee?", "options": ["No", "Yes", "Kinda"],
         "characters": {"Lorelai": 2, "Luke": 1, "Sookie": 1, "Jackson": 1, "Michelle": 2}},  # Corrected spelling here
        {"question": "What's your favorite book genre?", "options": ["Fiction", "Non-fiction", "Mystery"],
         "characters": {"Rory": 2, "Lorelai": 1, "Max Medina": 2, "Lane": 1}},
        {"question": "How do you handle stress?", "options": ["Stay calm", "Procrastinate", "Get emotional"],
         "characters": {"Rory": 2, "Dean": 1, "Jess": 2, "Sookie": 1}},
        {"question": "Pick a preferred mode of transportation:", "options": ["Car", "Motorcycle", "Walking"],
         "characters": {"Luke": 2, "Dean": 1, "Jess": 2}},
        {"question": "What's your favorite type of food?", "options": ["Fast food", "Home-cooked", "Exotic cuisine"],
         "characters": {"Rory": 1, "Lorelai": 2, "Sookie": 2, "Jackson": 1}},
        {"question": "How do you spend your weekends?", "options": ["Reading", "Watching TV", "Outdoor activities"],
         "characters": {"Rory": 2, "Lorelai": 1, "Dean": 1, "Jess": 2}},
        {"question": "What's your relationship with technology?", "options": ["Tech-savvy", "Average", "Technophobe"],
         "characters": {"Rory": 2, "Max Medina": 2, "Lane": 1}},
        {"question": "Pick a favorite season:", "options": ["Spring", "Summer", "Fall", "Winter"],
         "characters": {"Lorelai": 2, "Luke": 1, "Sookie": 1}},
        {"question": "Choose a coffee shop order:", "options": ["Black coffee", "Latte", "Tea"],
         "characters": {"Rory": 2, "Lorelai": 1, "Sookie": 2, "Michelle": 1}},
        {"question": "What's your approach to relationships?", "options": ["Commitment", "Independence", "Complicated"],
         "characters": {"Rory": 1, "Dean": 2, "Jess": 2, "Max Medina": 1}},
    ]

    # Iterate through the questions
    for question_data in questions:
        print(question_data["question"])
        for i, option in enumerate(question_data["options"], start=1):
            print(f"{i}. {option}")

        # Get the user's answer
        user_answer = input("Your choice (enter the corresponding number): ")

        # Update character scores based on the user's answer
        for character, score in question_data["characters"].items():
            character_scores[character] += score if user_answer == str(question_data["characters"][character]) else 0

    # Find the character with the highest score
    result_character = max(character_scores, key=character_scores.get)

    print("\nYou are most like", result_character, "!")
    print("Congratulations!")

def good_doctor_quiz():
    print("Welcome to The Good Doctor Character Quiz!")
    print("Answer the following 10 questions to find out which character you are.\n")

    # Initialize a dictionary to store the scores for each character
    character_scores = {
        "Dr. Shawn Murphy": 0,
        "Dr. Glassman": 0,
        "Dr. Claire": 0,
        "Dr. Andrew": 0,
        "Dr. Melendez": 0,
        "Lia": 0
    }

    # Questions and their corresponding characters' scores
    questions = [
        {"question": "How do you approach solving problems?",
         "options": ["Logically", "Emotionally", "Collaboratively"],
         "characters": {"Dr. Shawn Murphy": 2, "Dr. Glassman": 1, "Dr. Claire": 2, "Dr. Andrew": 1, "Dr. Melendez": 1,
                        "Lia": 2}},
        {"question": "What's your communication style?", "options": ["Direct", "Compassionate", "Analytical"],
         "characters": {"Dr. Shawn Murphy": 2, "Dr. Glassman": 2, "Dr. Claire": 1, "Dr. Melendez": 1, "Lia": 1}},
        {"question": "How do you handle high-pressure situations?",
         "options": ["Stay calm", "Get anxious", "Take charge"],
         "characters": {"Dr. Shawn Murphy": 2, "Dr. Glassman": 1, "Dr. Claire": 1, "Dr. Andrew": 2, "Dr. Melendez": 1}},
        {"question": "What's your attitude towards rules?",
         "options": ["Follow them strictly", "Question them", "Bend them when necessary"],
         "characters": {"Dr. Shawn Murphy": 1, "Dr. Claire": 2, "Dr. Andrew": 1, "Dr. Melendez": 2, "Lia": 1}},
        {"question": "Choose a medical specialty:", "options": ["Surgery", "Internal Medicine", "Pediatrics"],
         "characters": {"Dr. Shawn Murphy": 1, "Dr. Glassman": 1, "Dr. Claire": 2, "Dr. Andrew": 2, "Dr. Melendez": 1}},
        {"question": "How do you unwind after a long day?", "options": ["Read a book", "Listen to music", "Exercise"],
         "characters": {"Dr. Shawn Murphy": 1, "Dr. Glassman": 1, "Dr. Claire": 2, "Dr. Andrew": 2, "Dr. Melendez": 1}},
        {"question": "What's your stance on taking risks?",
         "options": ["Avoid them", "Calculated risks", "Embrace them"],
         "characters": {"Dr. Shawn Murphy": 1, "Dr. Glassman": 1, "Dr. Claire": 2, "Dr. Melendez": 2, "Lia": 1}},
        {"question": "Pick a favorite medical TV show:", "options": ["Grey's Anatomy", "House", "ER"],
         "characters": {"Dr. Shawn Murphy": 1, "Dr. Glassman": 2, "Dr. Andrew": 2, "Dr. Melendez": 1, "Lia": 1}},
        {"question": "What motivates you in your career?", "options": ["Helping others", "Achievement", "Advancement"],
         "characters": {"Dr. Shawn Murphy": 2, "Dr. Glassman": 1, "Dr. Claire": 2, "Dr. Melendez": 1, "Lia": 1}},
        {"question": "How do you handle conflicts with colleagues?",
         "options": ["Seek resolution", "Avoid confrontation", "Stand your ground"],
         "characters": {"Dr. Shawn Murphy": 2, "Dr. Glassman": 1, "Dr. Claire": 2, "Dr. Melendez": 1, "Lia": 1}},
    ]

    # Iterate through the questions
    for question_data in questions:
        print(question_data["question"])
        for i, option in enumerate(question_data["options"], start=1):
            print(f"{i}. {option}")

        # Get the user's answer
        user_answer = input("Your choice (enter the corresponding number): ")

        # Update character scores based on the user's answer
        for character, score in question_data["characters"].items():
            character_scores[character] += score if user_answer == str(question_data["characters"][character]) else 0

    # Find the character with the highest score
    result_character = max(character_scores, key=character_scores.get)

    print("\nYou are most like", result_character, "!")
    print("Congratulations!")

def harry_potter_quiz():
    print("Welcome to the Harry Potter Character Quiz!")
    print("Answer the following 10 questions to find out which character you are.\n")

    # Initialize a dictionary to store the scores for each character
    character_scores = {
        "Harry": 0,
        "Ron": 0,
        "Hermione": 0,
        "Pro. Severus Snape": 0,
        "Ginny": 0,
        "Lord Voldemort": 0,
        "Hagrid": 0,
        "Draco Malfoy": 0,
        "Sorting Hat": 0,
        "Cho": 0
    }

    # Questions and their corresponding characters' scores
    questions = [
        {"question": "What's your favorite subject at Hogwarts?",
         "options": ["Potions", "Transfiguration", "Defense Against the Dark Arts"],
         "characters": {"Pro. Severus Snape": 2, "Hermione": 2, "Ginny": 1, "Draco Malfoy": 1}},
        {"question": "Choose a magical creature:", "options": ["Hippogriff", "Phoenix", "Basilisk"],
         "characters": {"Harry": 1, "Ron": 1, "Hagrid": 2, "Lord Voldemort": 2}},
        {"question": "What's your Quidditch position?", "options": ["Seeker", "Chaser", "Keeper"],
         "characters": {"Harry": 2, "Ginny": 1, "Draco Malfoy": 1}},
        {"question": "Pick a wand core:", "options": ["Phoenix feather", "Dragon heartstring", "Unicorn hair"],
         "characters": {"Harry": 1, "Voldemort": 2, "Pro. Severus Snape": 1}},
        {"question": "What's your approach to magic?", "options": ["By the book", "Inventive", "Dark Arts"],
         "characters": {"Hermione": 1, "Ron": 2, "Lord Voldemort": 2, "Ginny": 1}},
        {"question": "Choose a magical sweet:",
         "options": ["Chocolate Frogs", "Bertie Bott's Every Flavor Beans", "Fizzing Whizzbees"],
         "characters": {"Harry": 1, "Ron": 2, "Ginny": 1, "Hermione": 2}},
        {"question": "What would you see in the Mirror of Erised?", "options": ["Fame", "Love", "Knowledge"],
         "characters": {"Harry": 1, "Ginny": 2, "Hermione": 2, "Pro. Severus Snape": 1}},
        {"question": "How do you feel about Slytherin House?", "options": ["Admire it", "Dislike it", "Neutral"],
         "characters": {"Harry": 2, "Ron": 1, "Hermione": 1, "Ginny": 2}},
        {"question": "What's your favorite spell?", "options": ["Expelliarmus", "Lumos", "Avada Kedavra"],
         "characters": {"Harry": 1, "Pro. Severus Snape": 2, "Lord Voldemort": 2, "Draco Malfoy": 1}},
        {"question": "Choose a magical artifact:",
         "options": ["Invisibility Cloak", "Elder Wand", "Resurrection Stone"],
         "characters": {"Harry": 2, "Lord Voldemort": 2, "Pro. Severus Snape": 1, "Ron": 1}},
    ]

    # Iterate through the questions
    for question_data in questions:
        print(question_data["question"])
        for i, option in enumerate(question_data["options"], start=1):
            print(f"{i}. {option}")

        # Get the user's answer
        user_answer = input("Your choice (enter the corresponding number): ")

        # Update character scores based on the user's answer
        for character, score in question_data["characters"].items():
            character_scores[character] += score if user_answer == str(question_data["characters"][character]) else 0

    # Find the character with the highest score
    result_character = max(character_scores, key=character_scores.get)

    print("\nYou are most like", result_character, "!")
    print("Congratulations!")

def choose_quiz():
    print("Choose a quiz:")
    print("1. Gilmore Girls")
    print("2. The Good Doctor")
    print("3. Harry Potter")

    choice = input("Enter the number of the quiz you want to take: ")

    if choice == "1":
        gilmore_girls_quiz()
    elif choice == "2":
        good_doctor_quiz()
    elif choice == "3":
        harry_potter_quiz()
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

# Call the function to choose a quiz
choose_quiz()
