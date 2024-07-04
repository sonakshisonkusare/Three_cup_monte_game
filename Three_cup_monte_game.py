# from random import shuffle
# mylist =[' ','0',' ']
# mixed_list =shuffle(mylist)


# def user_guess():
#     guess =''
#     while guess not in ['0','1','2']:
#         guess =input("Pick a number:0,1,2\n")
#     return int(guess)

# guess=user_guess()

# def check_guess(mixed_list,guess):
#     if mylist[guess] =='0':
#         print("Correct Guess")
#     else:
#         print("Incorrect guess!")
#         print(mylist)
#         print("Try Again....")
        
        
# check_guess(mixed_list,guess)

from random import shuffle

def shuffle_list():
    mylist = [' ', '0', ' ']
    shuffle(mylist)
    return mylist

def user_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1, 2\n")
    return int(guess)

def check_guess(mixed_list, guess):
    if mixed_list[guess] == '0':
        print("Correct Guess!")
    else:
        print("Incorrect guess!")
        print(f'The sequence of ball is: {mixed_list}')

while True:
    mixed_list = shuffle_list()
    guess = user_guess()
    check_guess(mixed_list, guess)
    
    play_again = input("Want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
