def add_items():
    a = input("Enter a name:  ")
    with open('tryal.txt','a') as f:
        f.write(a)
        f.write("\n")
        asking = input("Do you want to continue? Yes(Y) or No(N)  ")
        if asking == "Y" or asking == "y":
            add_items()
        else:
            print("Bye")
            f.close()
add_items()