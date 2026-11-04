# Created by Gianpaolo Demarchi
# Fork to your own repo, clone, copy this file and rename it with your initials,
# add it to git, push it and then ask for a Pull Request to my repo/upstream
# TL;DR: the only change to my repo should be a new helloWorldXX.py file with your name,
# nothing more ... but change a bit the content of this renamed file, to show some 
# commitment :-) 

print("✨ Welcome to my Python program! ✨")

name = input("Wie heißt du? ")
mood = input("Wie geht's dir heute? ")

print()
print(f"Hey {name}! 👋")

if mood.lower() == "gut":
    print("Das freut mich! Mach weiter so! 🚀")
elif mood.lower() == "schlecht":
    print("Kopf hoch! Morgen ist ein neuer Tag. 💛")
else:
    print(f"Danke, dass du deinen Tag als '{mood}' beschreibst!")

print("\n🎉 Thanks for testing my program!")
