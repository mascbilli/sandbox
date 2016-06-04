import sys
from random import randint


def getResponse():
	firstNum = randint(0,9)
	secondNum = randint(0,3)

	userAnswer = input("What is "+str(firstNum)+"^"+str(secondNum)+"?\n")
	return firstNum, secondNum, userAnswer


firstNum, secondNum, userAnswer = getResponse()

while userAnswer != "quit":

	if int(userAnswer) == firstNum**secondNum:
		print("correct!")
	else:
		print("incorrect! It's "+str(firstNum**secondNum))

	firstNum, secondNum, userAnswer = getResponse()

