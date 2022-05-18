# Hello World! Thanks for exploring the opportunity to join us at DataBased.
# We wish you the best with the assessment.
# Please complete and come prepared to present your solutions to the team.

# Instructions: Solve the problems listed below.
# There are more details about the problems in the provided README, we highly
# recommend reading through the README before solving the problems.

# In order to run the program install Python if not already installed.
# Then change your current directory to the same as the file
# Run the command `python DataBased_Python_Assessment.py` or `python3 DataBased_Python_Assessment.py`
# If you see 'PASSED' that means you passed the all test cases in the test function,
# it does not mean your solution is 100% correct. There may be edge cases you
# should add tests for on your own!

# PROBLEM 1 - Least Factorial
# Given an integer n, find the minimal k such that
# k = m! (where m! = 1 * 2 * ... * m) for some integer m; k ≥n. In other
# words, find the smallest factorial which is not less than n.


from logging import exception
from unittest import result


def leastFactorial(n):
    # TODO: Solve problem 1 here
    # temp: current number
    # fact: current factorial result
    temp = 2
    fact = 1

    while fact < n:
        fact = fact * temp
        temp+=1
    return fact

def testLeastFactorial():
    print('-' * 20)
    print('Part 1: Least Factorial')

    assert leastFactorial(17) == 24
    assert leastFactorial(5) == 6
    # TODO: add your own test cases here
    assert leastFactorial(1) == 1
    assert leastFactorial(17) == 24
    assert leastFactorial(5) == 6
    assert leastFactorial(106) == 120
    print('PASSED PROBLEM 1!')

# PROBLEM 2 - Reclying Lipstick
# You own a lipstick business. When a lipstick container is empty, there is actu-
# ally some leftover lipstick at the bottom that cannot be used because it is not
# accessible. Being an environmentally friendly business owner, you would like to
# recycle the leftover lipstick to make more. As a business, you know you need
# ‘numberOfLeftoversNeeded‘ to make a new lipstick. You have ‘numberOfLip-
# sticks‘ in your possession. What’s the total number of lipsticks you can sell
# assuming that each of your customers return their leftovers

def getTotalNumberOfLipsticks(numberOfLipsticks, numberOfLeftoversNeeded):
    # TODO: Solve problem 2 here
    result = numberOfLipsticks
    # recycle: the number to add into result for each round
    recycle = int(numberOfLipsticks / numberOfLeftoversNeeded)
    # left: the number left for each round
    left = numberOfLipsticks - recycle * numberOfLeftoversNeeded
    while recycle != 0:
        result += recycle
        temp =  recycle + left
        recycle = int((temp) / numberOfLeftoversNeeded)
        left = temp -  recycle * numberOfLeftoversNeeded

    return result

def testLipsticks():
    print('\n'+ '-' * 20)
    print('Part 2: Lipsticks')
    #print(getTotalNumberOfLipsticks(10,3))
    #assert getTotalNumberOfLipsticks(10, 3) == 9
    assert getTotalNumberOfLipsticks(10, 3) == 14
    assert getTotalNumberOfLipsticks(15, 5) == 18
    assert getTotalNumberOfLipsticks(2, 3) == 2
    # TODO: add your own test cases here
    assert getTotalNumberOfLipsticks(5, 2) == 9
    assert getTotalNumberOfLipsticks(10, 2) == 19
    assert getTotalNumberOfLipsticks(10, 5) == 12
    assert getTotalNumberOfLipsticks(10, 15) == 10
    assert getTotalNumberOfLipsticks(30, 2) == 59
    print('PASSED PROBLEM 2!')

# PROBLEM 3 - Students and Treats
# A school teacher wants to hand out treats to his students. The teacher de-
# cides the best way to divide the treats is to have the students sit in a circle of
# sequentially numbered chairs. A chair number will be drawn from a hat. Begin-
# ning with the student in drawn chair, one treat will be handed to each student
# sequentially going around the circle until all treats have been distributed.
# The teacher wants to have the students involved in sharing treats. He decides
# that whoever gets the very last treat, will be the student who makes the treats
# for the next game. Determine the chair number occupied by the student who
# will receive the last treat.

# For example, there are 4 students and 6 treats. The students arrange them-
# selves in seats numbered 1 to 4. Let’s suppose 2 is drawn from the hat. Students
# receive treats at positions 2,3,4,1,2,3. The student who gets the last treat is in
# chair number 3

def getLastStudent(numberOfStudents, treats, startingChair):
    # TODO: Solve problem 3 here
    # check edge case
    if treats <= 0 or numberOfStudents <=0 or startingChair <=0:
        raise ValueError("please input valid numbers")
    if startingChair > numberOfStudents:
        raise ValueError("please input a valid startingChair number")
    if numberOfStudents == 1:
        return 1

    times = int(treats / numberOfStudents)
    left = treats % numberOfStudents
    if times < 1:
        temp = treats + startingChair - 1
    else:
        temp = startingChair + left - 1
    temp = temp % numberOfStudents if temp > numberOfStudents else temp
    return temp

def testLastStudent():
        print('\n'+ '-' * 20)
        print('Part 3: Students and Treats')

        assert getLastStudent(5,2,1) == 2
        assert getLastStudent(5,2,2) == 3
        assert getLastStudent(7,19,2) == 6
        assert getLastStudent(3,7,3) == 3
        # TODO add your own test cases here
        assert getLastStudent(7,66,2) == 4
        assert getLastStudent(10,1,2) == 2
        try:
            getLastStudent(10,0,2)
        except ValueError:
            pass

        try:
            getLastStudent(1,10,2)
        except ValueError:
            pass

        try:
            getLastStudent(-1,10,2)
        except ValueError:
            pass

        try:
            getLastStudent(1,-10,2)
        except ValueError:
            pass
        
        try:
            getLastStudent(1,-10,-2)
        except ValueError:
            pass

        assert getLastStudent(1,10,1) == 1
        assert getLastStudent(100000000000000,1000000,11613131) == 12613130
        print('PASSED PROBLEM 3!')


# PROBLEM 4 - Pairs of Shoes
# Given an array of strings that represent a type of shoe, return how many matching
# pairs of shoes can be made?

def getPairsOfShoes(listOfShoes):
    # TODO: Solve problem 4 here
    #test edge case
    if listOfShoes is None:
        return 0

    table = {}
    for shoe in listOfShoes:
        if shoe not in table.keys():
           table[shoe] = 1
        else:
            table[shoe] += 1
    
    result = 0
    for _, value in table.items():
        result+= int(value/2)

    return result

def testPairsOfShoes():
    print('\n'+ '-' * 20)
    print('Part 4: Pairs of Shoes')
    assert getPairsOfShoes(["red", "blue", "red", "green", "green", "red"]) == 2
    assert getPairsOfShoes(["green", "blue", "blue", "blue", "blue", "blue", "green"]) == 3
    # TODO: Add your own test cases here
    assert getPairsOfShoes([]) == 0
    assert getPairsOfShoes(["red", "blue", "red", "green", "green", "red","red", "blue", "red", "green", "green", "red"]) == 6
    assert getPairsOfShoes(["red", "blue",  "green"]) == 0
    print('PASSED PROBLEM 4!')
    print('\n\nCongratulations!!')

# Call test functions
testLeastFactorial()
testLipsticks()
testLastStudent()
testPairsOfShoes()
