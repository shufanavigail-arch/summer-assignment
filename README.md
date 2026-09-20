This code is a game where the user needs to guess a randomly generated 4 letter
sequence made from DNA bases. In each guess, it will track the amount of bulls
(how many bases are right and in the right place) and the amount of cows
(how many bases are right but in the wrong place). By this it provides
information to enable the user to eventually guess the sequence correctly.

The main program, where you run the code is a file called "main.py", it's in the scripts folder. 

The programs output is in the file "results.txt". The output is the users' guess,
the amount of bulls, the amount of cows, in each guess. Until the user guesses
the sequence correctly.

code description:

The code has four function: 

Function 1 - "create_quartet" 
Generates a 4 letter sequence made of (not neccesarily all) A,T,C or G, and returns that sequence.

Function 2 - "validate"
The input is a sequence, the function makes sure the sequence is 
valid (4 letters long and made only of A,T,C,G). It returns False
if its invalid and True if its valid.

Function 3 - "find_bulls" 
The input is the users' guess and the randomly generated sequence. 
It compares both sequences and checks if the letters in each place
in the sequences are the same, if they are, it adds 1 to the number 
of bulls. If the letters in that place were not the same, it adds the
letter in the generated sequence to a variable called "rand_str", and
the letter in the users' guess to a variable called "guessed_str".
It returns the amount of bulls, and the two varibles - rand_str and guessed_str.

Function 4 - "find_cows"
The input is the two varibles created with function 3 - rand_str and guessed_str.
It checks if the letter in sub_guessed is in sub_rand, if it is,
it adds 1 to the number of cows.

A variable called attempts is added to track the users attempts, its initial value is 0.
The code then uses function 1, thus generating the random sequence. 
The users' guesss' variable begins as an empty sequence.
The code then starts a loop that runs while the users' sequence is different
from the generated sequence. Then, it asks the user to enter their guess.
It makes sure the users' guess is valid by using function 2. If it's invalid,
it prints an error message. If it's valid, it prints the guess, and then uses
funtions 3 and 4 to find the amount of bulls and cows. It then prints the amount 
of bulls and cows and adds 1 to attempts.
When the user guesses the sequence correctly, the loop stops and a message that
states the number of attempts it took to guess the sequence appears.

Code validation:

Variable "correct_seq" is used as a 4 letter sequence. A list of sequences
"sequences" is used as a comparing sequence. It contains invalid sequances,
as well as valid sequances for which we know the number of bulls and cows. 

