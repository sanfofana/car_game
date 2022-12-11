
print("Welcome to the Car Game!")

action = ""
started =  False

while True:
	action = input(">").lower()
	if action == "help":
		print("""
Start - To start
Stop - To Stop the car
quit - To quit
 """)
	elif action == "start":
		if started:
			print("Car has already been started")
		else:
			started = True
			print("Car started")
	elif action == "stop":
		if not started:
			print("Car has been stopped")
		else:
			started = False
			print("Car stopped")
		
	elif action == "quit":
		break
	
	else:
		
		print("I don't understand that")
