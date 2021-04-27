import os.path

import xlrd as xlrd
from xlwt import Workbook
from xlutils.copy import copy


def create():
    if os.path.exists("password.xlsx"):
        pass
    else:
        book = Workbook()
        sheet = book.add_sheet('password.xlsx')
        sheet.write(0, 0, "Application")
        sheet.write(0, 1, "Username")
        sheet.write(0, 2, "Password")
        sheet.write(0, 3, "Url")
        book.save('password.xlsx')


def enter_data():
    Application = input("Enter the name of application : ")
    Username = input("Enter Username: ")
    Password = input("Enter password: ")
    Url = input("Enter Url: ")

    rb = xlrd.open_workbook('password.xlsx', formatting_info=True)
    r_sheet = rb.sheet_by_index(0)
    r = r_sheet.nrows
    wb = copy(rb)
    sheet = wb.get_sheet(0)
    flag = 0
    for i in range(1, r_sheet.nrows):
        row_value = r_sheet.row_values(i)
        if row_value[0] == Application:
            update_permission = input("Data already exist. Want to update data. Enter Yes or No: ")
            if update_permission == "YES" or update_permission == "Yes" or update_permission == "yes" or update_permission == "Y" or update_permission == "y":
                sheet.write(i, 0, Application)
                sheet.write(i, 1, Username)
                sheet.write(i, 2, Password)
                sheet.write(i, 3, Url)
                flag = 1
                print("Value Updated")
            else:
                flag = 1

    if flag == 0:
        sheet.write(r, 0, Application)
        sheet.write(r, 1, Username)
        sheet.write(r, 2, Password)
        sheet.write(r, 3, Url)

    wb.save('password.xlsx')


def display_data():
    workbook = xlrd.open_workbook("password.xlsx")
    sheet = workbook.sheet_by_index(0)
    App = "Application"
    User = "Username"
    Pass = "Password"
    link = "Url"
    print(f"{App : <20}{User : ^20}{Pass : ^20}{link : >20}")

    for row in range(1, sheet.nrows):
        row_value = sheet.row_values(row)
        print(f"{row_value[0] : <20}{row_value[1] : ^20}{row_value[2] : ^20}{row_value[3] : >20}")


def update():
    Application = input("Enter the name of application: ")
    Username = input("Enter Username: ")
    Password = input("Enter password: ")
    Url = input("Enter Url: ")

    rb = xlrd.open_workbook('password.xlsx', formatting_info=True)
    r_sheet = rb.sheet_by_index(0)
    r = r_sheet.nrows
    wb = copy(rb)
    sheet = wb.get_sheet(0)
    flag = 0
    for i in range(1, r_sheet.nrows):
        row_value = r_sheet.row_values(i)
        if row_value[0] == Application:
                sheet.write(i, 0, Application)
                sheet.write(i, 1, Username)
                sheet.write(i, 2, Password)
                sheet.write(i, 3, Url)
                flag = 1
                print("Value Updated")


    if flag == 0:
        enter_permission = input("Data Not exist, Want to enter as new data. Type Yes or No: ")
        if enter_permission == "YES" or enter_permission == "Yes" or enter_permission == "yes" or enter_permission== "Y" or enter_permission == "y":
            sheet.write(r, 0, Application)
            sheet.write(r, 1, Username)
            sheet.write(r, 2, Password)
            sheet.write(r, 3, Url)
            print("Data entered as a new value")

    wb.save('password.xlsx')


def search():
    Application = input("Enter the name of application : ")
    workbook = xlrd.open_workbook("password.xlsx")
    sheet = workbook.sheet_by_index(0)
    flag = 0
    for row in range(1, sheet.nrows):
        row_value = sheet.row_values(row)
        if row_value[0] == Application:
            App = "Application"
            User = "Username"
            Pass = "Password"
            link = "Url"
            print(f"{App : <20}{User : ^20}{Pass : ^20}{link : >20}")
            print(f"{row_value[0] : <20}{row_value[1] : ^20}{row_value[2] : ^20}{row_value[3] : >20}")
            flag=1
            break

    if flag == 0:
        enter = input("Data does not exist, Want to save. Type Yes or No: ")
        if enter == "YES" or enter == "Yes" or enter == "yes" or enter== "Y" or enter == "y":
            enter_data()



if __name__ == "__main__":
    create()
    print("******************************************************************")
    print("***********************Password Manager***************************")
    print("******************************************************************")
    print("****************** Sfid : 258372**********************************")
    print("******************************************************************")
    print("\n\n")
    while(True):

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



