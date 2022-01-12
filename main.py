from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
print("Welcome to SoloPass: A Password Management Tool")
def view():
    file = open("database.txt", "r")
    data = file.readlines()
    file.close()
    if len(data) > 0:
        for info in data:
            info = info.split(",")
            print(info[0] + ". " + info[1])
        accountnumber = input("Enter account choice (type number): ")
        invalid = True
        for info in data:
            info = info.split(",")
            if accountnumber == info[0]:
                invalid = False
                print("Account Name:", info[1])
                print("Username:", info[2])
                print("Password:", info[3])
                break
        if invalid == True:
            print("You have entered invalid choice")
    else:
        print("No passwords available")
def add():
    file = open("database.txt", "r")
    data = file.readlines()
    file.close()
    account = input("Enter Account name: ")
    username = input("Enter Username: ")
    accountpassword = input("Enter Password: ")
    final_data = str(len(data) + 1) + "," + account + "," + username + "," + accountpassword
    file = open("database.txt", "w")
    if len(data) > 0:
        for line in data:
            file.write(line)
        file.write("\n")
    file.write(str(final_data))
    file.close()
    print("Password has been added!")
def delete():
    file = open("database.txt", "r")
    data = file.readlines()
    information = list(data)
    file.close()
    if len(data) > 0:
        for info in data:
            info = info.split(",")
            print(info[0] + ". " + info[1])
        accountnumber = input("Enter account choice(number): ")
        invalid = True
        for i in range(len(data)):
            data[i] = data[i].split(",")
            if accountnumber == data[i][0]:
                invalid = False
                information.pop(i)
                print("Password has been deleted!")
                listcount = 0
                # for i in range(len(data)):
                #   listcount += 1
                #   data.replace(data[i][0], listcount)
                break
        if invalid == True:
            print("Please enter a valid choice")
        file = open("database.txt", "w")
        for line in information:
            file.write(line)
        file.close()
    else:
        print("No passwords available")
def update():
    updatedPassword = input("What is your new master password? ")
    file = open("password.txt", "w")
    file.write(updatedPassword)
    file.close()
    print("Master password has been updated!")
while True:
    file = open("password.txt", "r")
    data = file.readlines()
    file.close()
    if len(data) == 0:
        masterpassword = input("What is your master password?")
        file = open("password.txt", "a")
        file.write(masterpassword)
        file.close()
    else:
        file = open("password.txt", "r")
        masterpassword = file.readline().strip()
        file.close()
        file = open("database.txt", "r")
        data = file.readlines()
        file.close()
        file = open("database.txt", "w")
        datalist = []
        for line in data:
            token = f.encrypt(bytes(str(line), 'utf-8'))
            datalist.append(token)
            file.write(str(token) + '\n')
        file.close()
    passwordattempt = input("Enter Master Password: ")
    if passwordattempt == masterpassword:
        file = open("database.txt", "r")
        data = file.readlines()
        file.close()
        file = open("database.txt", "w")
        for line in datalist:
            d = f.decrypt(line)
            file.write(d.decode())
        file.close()
        check = True
        while check:
            print("1. View Passwords")
            print("2. Add Passwords")
            print("3. Delete Passwords")
            print("4. Change Master Password")
            print("5. Log Out")
            option = input("What would you like to do? (type number) ")
            if option == "1":
                view()
            elif option == "2":
                add()
            elif option == "3":
                delete()
            elif option == "4":
                update()
            elif option == "5":
                break
        continue

    else:
        print("Incorrect Password. Try again.")
