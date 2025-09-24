import random

print("Welcome to the Math Quiz Tournament")
rounds = int(input("How many questions would you like to try? "))
score = 0
incorrect_answers = 0

for i in range(rounds):
    first = True
    
    print("Question number " + str(i+1))
    random_num = random.randint(1, 25)
    random_num1 = random.randint(1, 25)
    
    operator = random.randint(1,3)
   
    if operator == 1:
        correct_answer = random_num + random_num1
        print("Your question is ", random_num, "+", random_num1)
        
    elif operator == 2:
        correct_answer = random_num - random_num1
        print("Your question is ", random_num, "-", random_num1)
        
    elif operator == 3:
        correct_answer = random_num * random_num1
        print("Your question is ", random_num, "*", random_num1)

    answer = -1

    while answer != correct_answer:
        answer = int(input("Your answer (or 0 to quit): "))

        if answer == correct_answer:
            print("Correct!")
            score += 1
            if first == True:
                print("You got a bonus point!")
                score += 1
            
                
        elif answer == 0:
            print("Exiting this question...")
            break
            
        else:
            print("Wrong! Try again: ")
            incorrect_answers += 1
            first = False


print("Tournament over")
print()
print("Summary:")
print("Total questions: " + str(rounds))
print("Correct answers: " + str(score))
print("Incorrect answers: " + str(incorrect_answers))
