import random

def create_quartet(): #function that generates a random quartet of DNA bases
    bases = ["A", "T", "C", "G"]
    seq = ""
    for i in range(4):
        random_num = random.randrange(4)
        seq += bases[random_num]
    return seq

def validate(guess): #functions that checks if the input is valid (4 characters long and only contains A, T, C, G)
    if len(guess) != 4:
        return False
    for base in guess:
        if base not in ["A", "T", "C", "G"]:
            return False
    return True

def find_bulls(rand_str, guessed_str): #function that finds the number of bulls (how many bases are right and in the right place), sub_rand (the bases that are not bulls in the random sequence), and sub_guessed (the bases that are not bulls in the guessed sequence)

        Bulls = 0
        sub_rand = ""
        sub_guessed = ""
        for i in range(len(rand_str)): #checks number of bulls
            if rand_str[i] == guessed_str[i]:
                Bulls += 1
            else: #if the bases in i place are not the same, add them to the sub_rand and sub_guessed strings for cow calculation
                sub_rand += rand_str[i]
                sub_guessed += guessed_str[i]
        return Bulls, sub_rand, sub_guessed 

def find_cows(sub_rand, sub_guessed): #function that finds the number of cows (how many bases are right but in the wrong place)
        Cows = 0
        for base in sub_guessed: #checking if the bases who are not bulls in the guessed sequence are in the sub_rand string (the bases that are not bulls in the random sequence)
            if base in sub_rand:
                Cows += 1
                sub_rand = sub_rand.replace(base, "", 1)
        return Cows

correct_seq = create_quartet() #generates a random quartet of DNA bases

guess = ""

file = open("results/results.txt", "w")

attempts = 0  #tracks number of attempts
while guess != correct_seq: #loops until the user guesses the correct sequence
    guess = input("Guess the correct quartet (4 bases A, T, C, G): ")
    guess = guess.upper() #turns sequence into upper letters
    if not validate(guess): #checks if the input is valid (4 characters long and only contains A, T, C, G)
        print("Invalid input. Please enter a 4-character sequence using only A, T, C, or G.")
        file.write("Invalid input. Please enter a 4-character sequence using only A, T, C, or G.")
    if validate(guess): 
        file.write(guess + "\n")
        Bulls, sub_rand, sub_guessed = find_bulls(correct_seq, guess) #finds the amount of bulls
        Cows = find_cows(sub_rand, sub_guessed) #finds the amount of cows
        print(f"Bulls: {Bulls}, Cows: {Cows}")
        file.write(f"Bulls: {Bulls}, Cows: {Cows} \n")
        attempts += 1
print(f"Congratulations! You've guessed the correct quartet ({correct_seq}) after {attempts} attempts.")
file.write(f"Congratulations! You've guessed the correct quartet ({correct_seq}) after {attempts} attempts.")
file.close()

#code validation
sequences = ['ATCG','ako9','ATC','AATT', 'ATCGG', 'GHYS','AAAA']
correct_seq = 'AAAA'
for seq in sequences:
    if not validate(seq):
        print(seq)
        print(f"Invalid input. Please enter a 4-character sequence using only A, T, C, or G.")
    else:
        Bulls, sub_rand, sub_guessed = find_bulls(correct_seq, seq)
        Cows = find_cows(sub_rand, sub_guessed)
        print(f"Sequence: {seq}, Bulls: {Bulls}, Cows: {Cows}")
