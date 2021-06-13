import random
random_number = random.randint(0,100)
print(random_number)
count = 0
#print(count)
while True:


    guess_number = int(input("Enter The Guess Number: "))
    count += 1
    if random_number == guess_number:
        #print("Guess Number Is True")
        print("Congrats, Your Guess Number Is Correct")
        #total_count=count +1
        total_count = count
        print("Total Count Attempt: ", total_count)
        break

    elif random_number > guess_number:
        #count +1
        print("Random Number Is High, Guess Higher Number")
        #print(count)
    elif random_number < guess_number:
        #count +1
        print("Random Number Is Low, Guess Lower Number")
        #print(count)