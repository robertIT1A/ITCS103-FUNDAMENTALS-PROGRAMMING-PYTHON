while True:
    print("==== DREAMS FILE MANAGER ====")
    print("\n1. Read inspiring messages\n2. Add a new inspiring messages\n3. Rewrite the entire file\n4. Exit")
    ans = int(input("\n\nEnter your choice: "))

    if ans == 1:
        file = open("Guevarra Roberto - dreams.txt","r")
        content = file.read()
        file.close()
        print(content)
        print("\n\n")
    elif ans == 2:
        new = input("Enter Your new inspiring line: ")
        file = open("Guevarra Roberto - dreams.txt", "a")
        file.write(f"\n{new}")
        file.close()
        print("\nYour inspirational has been added")
    elif ans == 3:
        print("Warning: This will overwrite the file.")
        yes = input("Type YES to continue: ").upper()
        if yes == "YES":
           mess = input("Write your new set of inspiring messages: ")
           file = open("Guevarra Roberto - dreams.txt","w")
           file.write(mess)
           print("File has been overwritten.")
        else:
            print("\nFailed to overwrite the file\n")
    elif ans == 4:
        exit()
    else:
        print("Please enter the corresponding number!!!\n")
