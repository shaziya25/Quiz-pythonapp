# #  📌 Features We Can Add in Quiz App
# # ✅ Score Tracking
# # ✅ Random Question Order
# # ✅ Timer per Question
# # ✅ Levels (Easy, Medium, Hard)
# # ✅ Save Score to File (Leaderboard type)

# # QUIZ APPLICATION
# import random
# import time

# def load_questions(filename):

#     question =[] #--->empty list

#     try:
#         with open(filename,"r") as f:
#             data =f.read().strip().split("\n\n")
#             for block in data:
#                  lines = block.strip().split("\n")
#                  question =lines[0]
#                  options = lines[1:5]
#                  answer = lines[5].split(":")[1].strip()
#                  question.append((question, options, answer)) #-->store in tupple
         
#     except FileNotFoundError:
#            print(f"⚠️ File '{filename}' not found!")

#     return question     

# def ask_question(q,timer=10):
#      question , options ,  answer = q
#      print("\n"+question)
#      for opt in options:
#           print(opt)

#      start = time.time()
#      user_ans = input(f"Your Answer (A/B/C/D) within {timer}s:").strip().upper()
#      end =time.time()     


#      if end - start > timer:
#         print("⏰ Time Up!")
#         return False

#      return user_ans == answer


# def quiz(filename,timer=10):
#      question = load_questions(filename)
#      if not question:
#           return 0,0
#      random.shuffle(question)
#      score=0
#      for q in question:
#           if ask_question(q,timer):
#                print("✅ Correct!\n")
#                score +=1
#           else:
#                print("❌ Wrong!\n")

#           return score , len(question)


# def save_score(name,level,score,total):
#      with open("score.txt","a") as f:
#           f.write(f"{name},{level},{score}/{total}\n")


# def view_leaderboard():
#      try:
#           with open("score.txt","r") as f:
#               data =f.readlines()
#           if not data:
#             print("\nLeaderboard is empty!\n")
#             return
#      except FileNotFoundError:
#           print("\nNo leaderboard found yet!\n")
#           return     
     

#      scores =[]
#      for line in data:
#           name,level,score= line.strip().split(",")
#           gained, total = map(int,score.split("/"))
#           score.append(name,level,gained)

#           score.sort(key=lambda x:x[2], reverse= True)
#           print("\n--- 🏆 Leaderboard 🏆 ---")
#           for i, (name,level,score) in enumerate(score , start=1): #we use enumatre as rank as it shows index
#                print(f"{i}.{name} ({level})-{score} points")
#                print()



# # MAIN Menu
# def main(): #Iska matlab hai loop hamesha chalega (infinite loop).Yeh kab tak chalega? Jab tak tum break keyword use karke loop todh nahi dete.
#       print("🎯 Welcome to the Quiz App 🎯")
#       name = input("Enter your name: ")

#       while True:
#         print("\n--- Menu ---")
#         print("1. Play Quiz")
#         print("2. View Leaderboard")
#         print("3. Exit")
#         choice = input("Enter choice: ")
        
#         if choice == "1":
#             print("\nSelect Level:")
#             print("1. Easy\n2. Medium\n3. Hard")
#             level_choice = input("Enter level (1/2/3):")
#             if choice == "1":
#              level = "Easy"
#              filename ="easy.txt" 
#             elif choice =="2":
#              level = "Meduim"
#              filename ="meduim.txt"

#             elif level_choice == "3":
#                 level = "Hard"
#                 filename = "hard.txt"
#             else:
#                 print("Invalid level!")
#                 continue     

#             score , total = quiz(filename) 
#             print(f"{name}, Your score :{score}/{total}")
#             save_score(name,level,score,total) 

#         elif choice == "2":
#          view_leaderboard()

#         elif choice == "3":
#          print("Exiting... Goodbye!")
#         break

#       else:
#         print("Invalid choice! Try again.")

# if __name__ == "__main__":
#        main()


import random
import time

def load_questions(filename):
    questions = []  # Empty list to store all questions

    try:
        with open(filename, "r") as f:
            data = f.read().strip().split("\n\n")  # Split blocks with blank line

            for block in data:
                lines = block.strip().split("\n")

                question = lines[0]           # First line = question
                options = lines[1:5]          # Next 4 lines = options
                answer = lines[5].split(":")[1].strip().upper()  # "Answer: B" → B

                # Store in tuple and add to questions list
                questions.append((question, options, answer))

    except FileNotFoundError:
        print(f"⚠️ File '{filename}' not found!")

    return questions


def ask_question(q, timer=20):
    question, options, answer = q
    print("\n" + question)
    for opt in options:
        print(opt)

    start = time.time()
    user_ans = input(f"Your Answer (A/B/C/D) within {timer}s: ").strip().upper()
    end = time.time()

    if end - start > timer:
        print("⏰ Time Up!")
        return False

    return user_ans == answer


def quiz(filename, timer=20):
    questions = load_questions(filename)
    if not questions:
        return 0, 0

    random.shuffle(questions)
    score = 0

    for q in questions:
        if ask_question(q, timer):
            print("✅ Correct!\n")
            score += 1
        else:
            print("❌ Wrong!\n")

    return score, len(questions)


def save_score(name, level, score, total):
    with open("score.txt", "a") as f:
        f.write(f"{name},{level},{score}/{total}\n")


def view_leaderboard():
    try:
        with open("score.txt", "r") as f:
            data = f.readlines()

        if not data:
            print("\nLeaderboard is empty!\n")
            return

    except FileNotFoundError:
        print("\nNo leaderboard found yet!\n")
        return

    scores = []
    for line in data:
        name, level, score = line.strip().split(",")
        gained, total = map(int, score.split("/"))
        scores.append((name, level, gained))

    scores.sort(key=lambda x: x[2], reverse=True)

    print("\n--- 🏆 Leaderboard 🏆 ---")
    for i, (name, level, score) in enumerate(scores, start=1):
        print(f"{i}. {name} ({level}) - {score} points")
    print()


# MAIN Menu
def main():
    print("🎯 Welcome to the Quiz App 🎯")
    name = input("Enter your name: ")

    while True:
        print("\n--- Menu ---")
        print("1. Play Quiz")
        print("2. View Leaderboard")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            print("\nSelect Level:")
            print("1. Easy\n2. Medium\n3. Hard")
            level_choice = input("Enter level (1/2/3): ")

            if level_choice == "1":
                level = "Easy"
                filename = "easy.txt"
            elif level_choice == "2":
                level = "Medium"
                filename = "meduim.txt"
            elif level_choice == "3":
                level = "Hard"
                filename = "hard.txt"
            else:
                print("Invalid level!")
                continue

            score, total = quiz(filename)
            print(f"{name}, Your score: {score}/{total}")
            save_score(name, level, score, total)

        elif choice == "2":
            view_leaderboard()

        elif choice == "3":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
