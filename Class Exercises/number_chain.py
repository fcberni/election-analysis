#Using a while loop, ask the user "How many numbers?", then print out a chain of ascending numbers, starting at 0.
user_play = "y"
#After the results have printed ask the user if they would like to continue.
#If "y", restart the process, starting at 0 again.
#If "n", exit the chain.
while user_play == "y":

    user_number = int(input("How many numbers? "))

    for x in range(user_number):
        print(x)
#Rather than just displaying numbers constantly starting at 0, have the numbers begin at the end of the previous chain.
    user_play = input("Continue: (y)es or (n)o?")
 
