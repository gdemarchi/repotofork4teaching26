# Created by Gianpaolo Demarchi and I stole it
# Fork to your own repo, clone, copy this file and rename it with your initials,
# add it to git, push it and then ask for a Pull Request to my repo/upstream
# TL;DR: the only change to my repo should be a new helloWorldXX.py file with your name,
# nothing more ... but change a bit the content of this renamed file, to show some 
# commitment :-) 

def main():
    name = input("Enter your name here: ") 
    greeting = "Hello " + name
    print(greeting)
    answering_machine(greeting)

def answering_machine(inp):
    if inp.casefold().endswith("mick"):
        print("Please do not talk to me!")
    else:
        print("Thank god it's not him...")

main()
