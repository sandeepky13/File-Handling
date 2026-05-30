import os


file_name="data.txt"


while True:
    print("\n===============File CRUD Menu===================")
    print("1. Create")
    print("2. Update")
    print("3. Delete")
    print("4. Remane")
    print("5 Exit")

    choice=input("Enter Your Choice-->")


    if choice=="1":

        data=input("Input your data:")

        with open(file_name,"w") as f:
            f.write(data)
        print("=====================")
        print("file created successful:")

    elif choice=="2":
        new_data=input("Input New data:")
        with open(file_name,"w") as f:
            f.write(new_data)
        print("=====================")
        print("updation is successful")
    

    elif choice=="3":
        if os.path.exists(file_name):
            os.remove(file_name)
            print("=====================")
            print("file deleted successful")

        else:
            print("=====================")
            print("file does not exits")


    elif choice=="4":
        if os.path.exists(file_name):
            with open(file_name,"r") as f:
                print("=====================")
                print("\nfile data:")
                print(f.read())
        else:
            print("=====================")
            print("file does not exits")


    elif choice=="5":
        print("=====================")
        print("close the program")
        break
    
    else:
        print("=====================")
        print("Invalid your choice")



