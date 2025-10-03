import random

quiz_data = {
    "あ": "A",
    "い": "I",
    "う": "U",
    "え": "E",
    "お": "O",
    "か": "Ka",
    "き": "Ki",
    "く": "Ku",
    "け": "Ke",
    "こ": "Ko",
    "さ": "Sa",
    "し": "Shi",
    "す": "Su",
    "せ": "Se",
    "そ": "So",
    "た": "Ta",
    "ち": "Chi",
    "つ": "Tsu",
    "て": "Te",
    "と": "To",
    "な": "Na",
    "に": "Ni",
    "ぬ": "Nu",
    "ね": "Ne",
    "の": "No",
    "は": "Ha",
    "ひ": "Hi",
    "ふ": "Fu",
    "へ": "He",
    "ほ": "Ho",
    "ま": "Ma",
    "み": "Mi",
    "む": "Mu",
    "め": "Me",
    "も": "Mo",
}

def quiz():
    score = 0
    total_questions = len(quiz_data)
    
    print("Hiaragana Quiz\n")
    
    kanjis = list(quiz_data.keys())
    random.shuffle(kanjis)
    
    for kanji in kanjis:
        correct_answer = quiz_data[kanji]
        user_answer = input(f"What is {kanji} in alphabet? ")
        
        if user_answer.lower() == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"The correct answer is: {correct_answer}\n")
    
    print(f"Your final score is {score}/{total_questions}.")

quiz()
