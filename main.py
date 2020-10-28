import data
import login
import pip

pip.main(['install','PyNacl'])

x = "--->Hello This is a simple password manager<---" \
    "\n--->Given below are your commands" \
    "\n\n--->Enter 1 for adding a new user" \
    "\n--->Enter 2 for removing a user" \
    "\n--->Enter 3 for login " \
    "\n--->Enter 4 for exit"

data.file_checker()
login.file_checker()
def data1(current, username):
    y = 'Welcome ' + username + "!!"
    print(y)
    z = "\n--->Given below are some of your commands" \
        "\n--->Enter 1 to see your saved passswords" \
        "\n--->Enter 2 to add more passwords" \
        "\n--->Enter 3 to remove some of the saved passwords" \
        "\n--->Enter 4 to logout"
    while True:
        print(z)
        choice2 = int(input("Enter your choice\n-->"))
        if choice2 == 1:
            current.get_data()
            print('#'*15)
        elif choice2 == 2:
            name = input("Enter the username:\n")
            paswd = input('Enter the password:\n')
            site = input('Enter the name of site:\n')
            current.add_data(name, paswd, site)
            print('Done')
        elif choice2 == 3:
            site = input('Enter the name of site whose entry you want to remove:\n-->')
            current.remove_data(site)
        elif choice2 == 4:
            break


if __name__ == '__main__':
    while True:
        print(x)
        choice = int(input('Enter you choice:\n-->'))
        if choice == 1:
            username = input("Enter a username:\n-->")
            paswd = input('Enter a password:\n-->')
            result = login.user_add(username, paswd)
            if result:
                print("User added!!\nYou can now login\n")
            else:
                print("Failed, that username is already used ,you can try another name")
        elif choice == 2:
            username = input("Enter the username you want to delete\n-->")
            paswd = input('Enter the password\n-->')
            result = login.user_remove(username, paswd)
            if result:
                print('User successfully removed!!')
            else:
                print('Username or password is invalid!!\n Please try again')
        elif choice == 3:
            username = input('Enter your username:\n-->')
            passwd = input('Enter your password\n-->')
            current_user = data.User(username, passwd)
            res = current_user.usercheck()
            if res == False:
                print('Invalid password!!\nTry again')
            else:
                data1(current_user, username)

        elif choice == 4:
            print("Thankyou for using this software!!")
            break
