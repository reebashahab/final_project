# Import the choice() function from the random module to return a random item from our list later on.
from random import choice

#Define some variables.
u = 0 #User's starting score.
v = 0 #Computer's starting score score.
rounds = 1 #The number of rounds that have passed. Will increment.
rps = ['r', 'p', 's'] #List containing rock, paper, or scissors (from which computer will randomly pick.)

#Define game function. As long as the number of rounds that have passed <= the number of rounds selected, will loop. Scores will increment each round, as will the number of rounds passed.
def game(rounds, number_of_rounds, u, v):
	while rounds <= number_of_rounds:
		print """\nR: Rock,
P: Paper,
S: Scissor\n"""
		user = raw_input("What is your weapon of choice? ")   
		user = user.lower() #formats user choice to match items in list
		py = choice(rps) #randomly picks computer's choice

		rounds+=1 #at the end of each round, increments by 1
		
		#sets the rules
		if user[0].lower() == py[0].lower():
			print "You and I both had picked",py.upper()+". It's a tie. No points!"
		elif user[0].lower() == 'r' and py[0].lower() == 's':
			print "Oh no! You picked rock, I picked scissors. 1 point for you!"
			u+=1
		elif user[0].lower() == 'r' and py[0].lower() == 'p':
			print "Hey, you picked rock, I picked paper! 1 point for me! :)"
			v+=1
		elif user[0].lower() == 's' and py[0].lower() == 'p':
			print "Oh no! You picked scissors, I picked paper. 1 point for you!"
			u+=1
		elif user[0].lower() == 's' and py[0].lower() == 'r':
			print "Hey, you picked scissors, I picked rock! 1 point for me! :)"
			v+=1
		elif user[0].lower() == 'p' and py[0].lower() == 's':
			print "Hey, you picked paper, I picked scissors. 1 point for me! :)"
			v+=1
		elif user[0].lower() == 'p' and py[0].lower() == 'r':
			print "Oh no! You picked paper, I picked rock. 1 point for you!"
			u+=1
		#invalid choice
		elif user[0].lower() not in ['r', 'p', 's', 'e']:
			print "That's not a valid choice. Try again."
			rounds = rounds - 1
		#just exit, and give me score
		elif user[0].lower() == "e":
			break
	#if the user has more points...
	if u > v:
		print "\n-----\nYOU WIN, with a final score of",str(u),"to",str(v)+"! You da best, "+name+"!\n-----"
		play_choice = raw_input("\nPlay again? y/n ")
		play_choice = play_choice[0].lower()
		play(play_choice)
	#if the computer has more points
	elif u < v:
		print "\n-----\nI WIN, with a final score of",str(v),"to",str(u)+"! You were a worthy opponent.\n-----"
		play_choice = raw_input("\nPlay again? y/n ")
		play_choice = play_choice[0].lower()
		play(play_choice)
	#if it's a tie, will ask for a sudden tie break round, and recall the function with some new arguments.
	elif u == v:
		print "\nIt's a tie! Final score is",str(v),"to",str(u)+"."
		play_choice = raw_input("\nTie breaker round? y/n ")
		if play_choice[0].lower() == "y":
			game(1, 1, u, v)
		else: 
			print "Okay, see you later!"

#define play function that sets up for the game
def play(play_choice):
	#if they want to play, will ask for number of rounds. Max 5.
	if play_choice[0].lower() == "y":
		print "\nSweet! Here are the rules: Rock breaks Scissors, Scissors cuts Paper, and Paper beats Rock."
		number_of_rounds = raw_input("\nHow many rounds do you want to play? Please limit to 5. ")
		while number_of_rounds.isdigit() == False:
			number_of_rounds = raw_input("\nHm, that's not a valid input. \nPlease pick a number <= 5. ")
		else:
			number_of_rounds = int(number_of_rounds)
			while number_of_rounds > 5:
				number_of_rounds = int(raw_input("Please pick a number <= 5. "))
			else:
				print "\nGot it!",str(number_of_rounds),"round(s). Let's get ready to rumble! \n(Please type 'exit', if you'd like to quit and go to final scores at any point.)"
				game(rounds, number_of_rounds, u, v) #calls game function once they've indicated they want to play, and have selected the app. number of rounds.
	#if they'd rather not play, will exit you out.
	elif play_choice[0].lower() == "n":
		print "\nOkay! Stay awesome."
	#if you enter something invalid, will prompt you to try again.
	else:
		play_choice = raw_input("\nHm, that's not a valid choice. Please try again. y/n ")
		play_choice = play_choice[0].lower()
		play(play_choice)
		
		
name = raw_input("What's your name, friend? ") #ask for player's name
name = name.capitalize() #formats player's name
play_choice = raw_input("\nHi " + name + "! Do you want to play rock, paper, scissors with me? y/n ") #ask whether they want to play r,p,s

play(play_choice) #call the play function and begin!
		