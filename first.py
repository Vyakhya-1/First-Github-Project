#program to play a game of stone paper scissors with the computer
from random import randint #importing randit to generate random integers for computer
comp=0 #initial score of the computer
user=0 #initial score of the user
print ('Do you want to play?')
a=input('Enter yes or no') #entering the choice to play or not
if a=='yes':
	def show(): #function to show the menu
		print ('Enter 1 for scissors')
		print ('Enter 2 for stone')
		print ('Enter 3 for paper')
while ((user<5) and (comp<5) and (a=='yes')): #cheking the condition for the number of iterations
	show() #printing menu by calling the function
	u=int(input('Enter your choice')) #entering the choice by the user
	c=randint(1,3) #generation of random int between 1to 3 for computer
	print ('My choice is',c)
	if u==c: #if both the choices are same
		print ('Its a tie')
		comp+=1 #updating scores
		user+=1
	elif(u==3 and c==1): #if different chices are generated then displaying appropriate message and updating scores
		print ('Yay!I won')
		comp+=1
	elif(u==3 and c==2):
		print ('Uggh!I lost')
		user+=1
	elif(u==1 and c==2):
		print ('Yay!I won')
		comp+=1
	elif(u==1 and c==3):
		print ('Uggh!I lost')
		user+=1
	elif(u==2 and c==1):
		print ('Uggh!I lost')
		user+=1
	elif(u==2 and c==3):
		print ('Yay!Iwon')
		comp+=1
	else: #if an integer beyond beyond the range is entered
		print('Invalid choice')
		continue
if comp>user: #if computer scores 5 first
	print ('I won the match!')
	print ('My score is',comp)
	print ('Your score is',user)
else: #if user scores 5 first
	print ('You have won the match')
	print ('My score is',comp)
	print ('Your score is',user)
print ('Do you like to contibue?') #asking user to continue
a=input('Enter yes or no again') #taking choice from the user again and updating it for while loop condition
