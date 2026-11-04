# Created by Gianpaolo Demarchi
# Fork to your own repo, clone, copy this file and rename it with your initials,
# add it to git, push it and then ask for a Pull Request to my repo/upstream
# TL;DR: the only change to my repo should be a new helloWorldXX.py file with your name,
# nothing more ... but change a bit the content of this renamed file, to show some 
# commitment :-)

print("Hello Gianpaolo!")

print("Lass uns ein Spiel spielen! \nDeine Aufgabe: Finde den Ausgang!")

weg = input("Du kannst dich entscheiden.\nEntweder oben; unten; links oder rechts. \nGebe nur das passende Wort ein (kleingeschrieben)! \n")

if weg != "rechts":
    print("Du bist direkt falsch abgebogen. Das war wohl nichts :(")
else:
    print("Das war die goldrichtige Entscheidung!")
    print("Als nächstes musst du eine Matrix lösen - dot product")

    # Matrix ausgeben
    print("Matrix A: \n[1, 4 \n3, 2]")
    print("Matrix B. \n[3, 1 \n4, 2]")

    ergebnis = int(input("Welche Zahl steht im Ergebnis oben rechts?"))
    # Überprüfung der Antwort
    if ergebnis == 12:
        print("Hast du seit dem letzten Mal nochmal geübt? \nDie Lösung ist richtig! Du bist draußen!")
    else:
        print("Also entweder war deine Eingabe fehlerhaft. \nOder du solltest nochmal üben!")