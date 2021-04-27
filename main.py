from Function import *
if __name__ == "__main__":
    create()
    print("******************************************************************")
    print("***********************Password Manager***************************")
    print("******************************************************************")
    print("***********************Sfid : 258372******************************")
    print("******************************************************************")
    print("\n\n")
    while True:
        print("Select from Below Options: ")
        print("1. Enter\n"
              "2. Display\n"
              "3. Update\n"
              "4. Search\n"
              "5. Exit\n")
        option = int(input())
        if option == 1:
            enter_data()
        elif option == 2:
            display_data()
        elif option == 3:
            update()
        elif option == 4:
            search()
        elif option == 5:
            break
        else:
            print("Select Correct option")



