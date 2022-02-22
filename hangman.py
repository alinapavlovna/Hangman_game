from random import randint
import string
import os 
from rich.console import Console

console = Console(width=300)


def pick_complexity():

    console.print("[magenta]Choose the level of game:\n1.Easy\n2.Medium\n3.Hard")
    answ = input()

    filename = ""
    if answ == "1":
        filename = "words_l1.txt"
    elif answ == "2":
        filename = "words_l2.txt"
    elif answ == "3":
        filename = "words_l3.txt"
    else:
        filename = "words_l1.txt"
    return filename



def read_from_file(filename, words):
    file = open(filename, "r")

    while True:
        line = file.readline().strip('\n')
        if not line:
            break
        words.append(line)    
    file.close


'''
def write_to_file(rate_dict):
    with open('rate.txt','a') as out:
        for key,val in rate_dict.items():
            out.write('{}:{}\n'.format(key,val))
'''

#pick_complexity()
def check(value):
    if len(value) > 1:
        #print("Please, enter ONE letter")
        return False
    if value == '':
        #print("Please, enter a letter")
        return False
    #for letter in value: 
    if value not in string.ascii_lowercase: 
        return False
    return True
    


def restart_or_quite():
    ans = console.input("[purple]Would you like to play again? (y/n): ").lower()
    if ans == "y":
        main()




def welcome_to_hangman():
    console.print("     ___      ___         ___         ____       ___   ____________   ____          ____         ___         _____       ___                   ", style="bold italic yellow")
    console.print("    |   |    |   |       \   \       |    \     |   | |    ________| |    \        \    |       \   \       |     \     |   |       ",style="bold italic yellow")
    console.print("    |   |    |   |      \  \  \      |     \    |   | |   |          |     \      \     |      \  \  \      |      \    |   |         ", style="bold italic yellow")
    console.print("    |   |____|   |     \  \ \  \     |   \  \   |   | |   |   _____  |   |\ \    \ \|   |     \  \ \  \     |   |\  \   |   |     ", style="bold italic yellow")
    console.print("    |    ____    |    \  \___\  \    |   |\  \  |   | |   |  |_    | |   | \ \  \ \ |   |    \  \___\  \    |   | \  \  |   |        ", style="bold italic yellow")
    console.print("    |   |    |   |   \   _____   \   |   | \  \ |   | |   |    |   | |   |  \ \ \ \ |   |   \   _____   \   |   |  \  \ |   |              ", style="bold italic yellow")
    console.print("    |   |    |   |  \  \       \  \  |   |  \  \|   | |   |____|   | |   |   \___/  |   |  \  \       \  \  |   |   \  \|   |               ", style="bold italic yellow")
    console.print("    |___|    |___| \__\         \__\ |___|   \_____ | |____________| |___|          |___| \__\         \__\ |___|    \______|                ", style="bold italic yellow")
    console.print()
    print()


def print_hangman(tries):
    if tries == 6:
        console.print("[green]________      ")
        console.print("[green]|      |      ")
        console.print("[green]|             ")
        console.print("[green]|             ")
        console.print("[green]|             ")
        console.print("[green]|             ")
        print("\n")

        
    elif tries == 5:
        console.print("[green]________      ")
        console.print("[green]|      |      ")
        console.print("[green]|      0      ")
        console.print("[green]|             ")
        console.print("[green]|             ")
        console.print("[green]|             ")
        print("\n")

        
    elif tries == 4:
        console.print("[green]________      ")
        console.print("[green]|      |      ")
        console.print("[green]|      0      ")
        console.print("[green]|     /       ")
        console.print("[green]|             ")
        console.print("[green]|             ")
        print("\n")

        
    elif tries == 3:
        console.print("[green]________      ")
        console.print("[green]|      |      ")
        console.print("[green]|      0      ")
        console.print("[green]|     /|      ")
        console.print("[green]|             ")
        console.print("[green]|             ")
        print("\n")

       
    elif tries == 2:
        console.print("[green]________      ")
        console.print("[green]|      |      ")
        console.print("[green]|      0      ")
        console.print("[green]|     /|\     ")
        console.print("[green]|             ")
        console.print("[green]|             ")
        print("\n")

        
    elif tries == 1:
        console.print("[green]________      ")
        console.print("[green]|      |      ")
        console.print("[green]|      0      ")
        console.print("[green]|     /|\     ")
        console.print("[green]|     /       ")
        console.print("[green]|             ")
        
    elif tries == 0:   
        console.print("[red]________      ")
        console.print("[red]|      |      ")
        console.print("[red]|      0      ")
        console.print("[red]|     /|\     ")
        console.print("[red]|     / \     ")
        console.print("[red]|             ")
        print("\n")

    

    
def main():
    alphabet = "a/b/c/d/e/f/g/h/i/j/k/l/m/n/o/p/q/r/s/t/u/v/w/x/y/z"
    rate_dict = {}
    words = []
    os.system('clear')
    welcome_to_hangman()

    username = console.input("[magenta]Enter your name: ")
    console.print(f"Hello, {username}!Let's start a game!", style="bold italic yellow")

    rate_dict[username] = 0
    filename = pick_complexity()
    #print(filename)
    read_from_file(filename, words)

    #print(words)

    index = randint(0, len(words)-1)

    user_word = words[index]
    j = 0
    res = []
    while j < len(user_word):
        if user_word[j] not in string.ascii_lowercase: 
            res.append(user_word[j])
        elif user_word[j] == " ":
            res.append(" ")
        else:
            res.append(" _ ")
        j += 1
 

    tries_total = 6
    tries = 6
    #print("Print one letter to guess")
    #print(alphabet)

    while tries:
        os.system('clear')
        welcome_to_hangman()
        #print(f"*** word: {user_word} ***")

        #print_hangman(tries)

        console.print("Tries left: ", tries, f"/ {tries_total}", style="bold italic red")
        print()
        console.print("Try to guess the word", style="bold italic purple")
        res_str = ''.join(res)
        print()
        console.print(res_str, style="bold italic purple")
        print()

        print_hangman(tries)

        print()
        print("Print one letter to guess")
        console.print(alphabet, style="bold italic blue")
        print()

        '''
        if tries < 3:
            answ = console.input("[yellow]Are you want a hint?(y/n)")
            if answ == "y":
                answ1 = int(console.input("[yellow]Input the number of letter you want to unhide?(1-9)"))
                while answ1 > len(user_word) or answ1 < 1:
                    console.print("[red]There is no letter with this index, try again...")
                    answ1 = int(console.input("[yellow]Input the number of letter you want to unhide?(1-9)"))
                #res[answ1-1] = user_word[answ1-1]
                console.print(f"The {answ1} letter is {user_word[answ1-1]}", style="bold italic purple")
                tries -= 1
        '''

        letter = console.input(f"[green]Enter a letter: [green]").lower()

        if check(letter):
            if letter in user_word:
                i = 0
                while i < len(user_word):
                    if letter == user_word[i]:
                        res[i] = user_word[i]
                    i+=1
                
                rate_dict[username] += 1
                alphabet = alphabet.replace(letter, ' ') 

            else:
                
                if letter in alphabet:
                    tries -= 1
                alphabet = alphabet.replace(letter, ' ')


            res_str = ''.join(res)
            if res_str == user_word:
                os.system('clear')
                welcome_to_hangman()
                console.print(f"[green]Congratulations! You won the game! The word was '{res_str}'")
                
                
                answ = console.input("[blue]Are you want to check rating of the Hangman?")
                if answ == "y":
                    console.print(rate_dict, style="bold italic purple")
                #console.print(f"[green]Your rate in Hangman is {rate_dict[username]}")
                restart_or_quite()
                break

            print(res_str)
    print()
    if tries == 0:
        os.system("clear")
        welcome_to_hangman()
        print_hangman(tries)
        console.print(f"[red]Sorry, you lost...The word was '{user_word}'")
        answ = console.input("[blue]Are you want to check rating of the Hangman?")
        if answ == "y":
            console.print(rate_dict, style="bold italic purple")

        restart_or_quite()


if __name__ == "__main__":
    main()
                    


