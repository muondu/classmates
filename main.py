def logic():
    a = input("Enter one name:  ")
    print("You entered: " + a)

    with open('main.txt','a') as f:
        f.write(a)
        f.write("\n")
        def input_algorithim():
            continu_e = input("Do you want to enter another name? Kindly choose Yes(Y) or no(N)? ")
            if continu_e == "Y" or continu_e == "y":
                logic()
            elif continu_e == "N" or continu_e == "n":
                print("Thank you.")
                f.close()
            else:
                print("You did not chose an option above!")
                input_algorithim()
        input_algorithim()

logic()