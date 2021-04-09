import os

q = "C:/terminal-notes/"
path = q  

if os.path.exists(q):
    print("Enter Your Command or Type \"Help\":")
    x = input()
    y = x.lower()

    if y == "help":
        print("")
        print("Commands")
        print("- New (Creates Note)")
        print("- Read (Prints Out Note Text Into Command Line)")
        print("- Append (Adds To The End Of A Note)")
        print("- Edit (Open Note In Notepad For Editing)")
        print("- Delete (Delete Note)")

    elif y == "new":
        print("")
        z = input("Name of File: ")
        print("Creating A New File...")
        f = open(q + z + ".txt", "w+")
        print("Write your note:")
        a = input()
        f.write(a)
        f.close()

    elif y == "read":
        print("")
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.lower().endswith('.txt'):
                    print ("- " + file.rsplit( ".", 1 )[ 0 ])
        print("")
        b = input("Which Note? ")
        print("")
        g = open(q + b + ".txt", "r")
        contents = g.read()
        print(contents)

    elif y == "append":
        print("")
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.lower().endswith('.txt'):
                   print ("- " + file.rsplit( ".", 1 )[ 0 ])

        print("")
        c = input("Which File Would You Like To Edit? ")
        h = open(q + c + ".txt", "r")
        contents2 = h.read()
        print("")
        print(contents2)
        h.close()
        print("")
        j = open(q + c + ".txt", "a")
        d = input("What Would You Like To Append ")
        j.write(" " + d)
        j.close()

    elif y == "edit":
        print("")
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.lower().endswith('.txt'):
                   print ("- " + file.rsplit( ".", 1 )[ 0 ])
        print("")
        e = input("Which File Would You Like To Edit? ")
        f = q + e + ".txt"
        os.system('notepad.exe' + " " + f)

    elif y == "delete":
        print("")
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.lower().endswith('.txt'):
                   print ("- " + file.rsplit( ".", 1 )[ 0 ])
        print("")
        deleteinput = input("Which File Would You Like To Delete? ")
        deletepath = q + deleteinput + ".txt"
        os.remove(deletepath)
    print("")
    input("Press Any Key To Exit")
else:
    os.mkdir(path)