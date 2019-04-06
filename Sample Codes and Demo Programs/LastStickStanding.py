from time import sleep

### Global variables
move_count = 0
stick_count = 99 # Overriden in user input
limit = 5 # Overriden in user input

### Functions

def print_stick():
    print("[", end="")
    for _ in range(stick_count):
        print ("\u25AE", end="")
        sleep(0.1)
    print("]  {} stick(s) remaining".format(stick_count))
		
def player_move():
    
    global stick_count
    n = 0
    while (n <= 0 or n > limit):
        n = int(input ("\n Player to move (enter a number): "))                 
    stick_count = stick_count - n
	
def computer_move():
	global stick_count
	t = limit + 1
	to_remove = stick_count % t
	if (to_remove == 0):
	    to_remove = limit
	print ("\n Computer to move: ", to_remove)
	stick_count -= to_remove 
	
def play():
    global move_count
    while stick_count > 0:
        print_stick()
        if move_count % 2 == 0:
            computer_move()
        else:
            player_move()
        move_count+=1

    print_stick() 
    if move_count%2 ==1:
        print("**COMPUTER WIN!**")
    else:
        print("**PLAYER WIN!**")
		
### Commands
		
stick_count = int (input ("How many sticks to play with? "))
limit = int (input ("How many sticks can be removed each time? "))
play()

input("\n Press any key to exit")
	
	
