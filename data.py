import encryption
import pickle
import login


class User:
    '''for maintaing a instance of each user'''

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.key = login.verify(username, password)

    def usercheck(self):
        '''Checks if the username and the password matches'''
        if not self.key:
            return False
        else:
            return True

    def get_data(self):
        file = open("data.txt", 'rb')
        dictionary = pickle.load(file)
        file.close()
        data = dictionary[self.username]
        print("username---password---sitename")
        for i in data:
            for j in i:
                unencoded = encryption.decrypter(j, self.key)
                print(unencoded.decode(), end="---")
            print("")

    def add_data(self, username1, password1, sitename):
        username1 = username1.encode()
        password1 = password1.encode()
        sitename = sitename.encode()
        file = open('data.txt', 'rb')
        dictionary = pickle.load(file)
        file.close()
        data = dictionary[self.username]
        entry = (encryption.encrypter(username1, self.key), encryption.encrypter(password1, self.key),
                 encryption.encrypter(sitename, self.key))
        data.append(entry)
        dictionary[self.username] = data
        file = open('data.txt', 'wb')
        pickle.dump(dictionary, file)
        file.close()

    def remove_data(self, sitename):
        file = open('data.txt', 'rb')
        dictionary = pickle.load(file)
        file.close()
        data = dictionary[self.username]
        count = 0
        while count < len(data):
            if encryption.decrypter(data[count][2], self.key) == sitename.encode():
                data.pop(count)
            else:
                print("site doesnt exist")
            count += 1
        dictionary[self.username] = data
        file = open('data.txt', 'wb')
        pickle.dump(dictionary, file)
        file.close()


def file_checker():
    try:
        file = open("data.txt", "rb")
    except FileNotFoundError:
        file = open('data.txt', 'wb')
        pickle.dump({}, file)
    file.close()
