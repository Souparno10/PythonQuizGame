print('Welcome to my Python Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=5
 
if answer.lower()=='yes':
    answer=input('Question 1: I which programming language is this written?')
    if answer.lower()=='python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: Is this made in Python?')
    if answer.lower()=='yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: Did you like this program?')
    if answer.lower()=='yes
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
print('Thank You for playing this quiz game, you answered',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('Bye!')