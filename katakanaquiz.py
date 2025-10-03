import random

quiz_data = {
    "ア": "A",
    "イ": "I",
    "ウ": "U",
    "エ": "E",
    "オ": "O",
    "カ": "Ka",
    "キ": "Ki",
    "ク": "Ku",
    "ケ": "Ke",
    "コ": "Ko",
    "サ": "Sa",
    "シ": "Shi",
    "ス": "Su",
    "セ": "Se",
    "ソ": "So",
    "タ": "Ta",
    "チ": "Chi",
    "ツ": "Tsu",
    "テ": "Te",
    "ト": "To",
    "ナ": "Na",
    "ニ": "Ni",
    "ヌ": "Nu",
    "ネ": "Ne",
    "ノ": "No",
    "ハ": "Ha",
    "ヒ": "Hi",
    "フ": "Fu",
    "ヘ": "He",
    "ホ": "Ho",
    "マ": "Ma",
    "ミ": "Mi",
    "ム": "Mu",
    "メ": "Me",
    "モ": "Mo",
}

def quiz():
    score = 0
    total_questions = len(quiz_data)
    
    print("Katakana Quiz\n")
    
    kanas = list(quiz_data.keys())
    random.shuffle(kanas)
    
    for kana in kanas:
        correct_answer = quiz_data[kana]
        user_answer = input(f"What is {kana} in alphabet? ")
        
        if user_answer.lower() == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"The correct answer is: {correct_answer}\n")
    
    print(f"Your final score is {score}/{total_questions}.")

quiz()