import os

q = "C:/terminal-notes/"
path = q  

if os.path.exists(q):
    print("Enter Your Command or Type \"Help\":")
    x = input()
    y = x.lower()

    if y == "help":
        print("Commands")
        print("- New (Creates Note)")
        print("- Read (Prints Out Note Text Into Command Line)")
        print("- Append (Adds To The End Of A Note)")
        print("- Edit (Open Note In Notepad For Editing)")
        print("- Delete (Delete Note)")

    elif y == "new":
        print("Name of File:")
        z = input()
        print("Creating A New File...")
        f = open(q + z + ".txt", "w+")
        print("Write your note:")
        a = input()
        f.write(a)
        f.close()

    elif y == "read":
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.lower().endswith('.txt'):
                    print (file)
        print("Which Note?")
        b = input()
        g = open(q + b + ".txt", "r")
        contents = g.read()
        print(contents)

    elif y == "append":
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.lower().endswith('.txt'):
                    print (file)

        print("which file would you like to edit?")
        c = input()
        h = open(q + c + ".txt", "r")
        contents2 = h.read()
        print(contents2)
        h.close()
        print("What would you like to append")
        j = open(q + c + ".txt", "a")
        d = input()
        j.write(" " + d)
        j.close()

    elif y == "edit":
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.lower().endswith('.txt'):
                    print (file)
        print("Which File Would You Like To Edit?")
        e = input()
        f = q + e + ".txt"
        os.system('notepad.exe' + " " + f)

    elif y == "delete":
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.lower().endswith('.txt'):
                    print (file)
        print("Which File Would You Like To Delete")
        deleteinput = input()
        deletepath = q + deleteinput + ".txt"
        os.remove(deletepath)
    input("Press Any Key To Exit")
else:
    os.mkdir(path)