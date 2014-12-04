# Testing out making a test based adventure



def main():

	while quit == False:

		command = ""
		command = input("What do you do?")

		command = command.split(' ')

		if command[0] == "quit":
			quit = True

main()