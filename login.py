import encryption
import pickle


def file_checker():
    try:
        file = open("userlist.txt", "rb")
    except FileNotFoundError:
        file = open('userlist.txt', 'wb')
        pickle.dump([], file)
    file.close()


def verify(username, password):
    file = open("userlist.txt", 'rb')
    data = pickle.load(file)
    file.close()
    count = 0
    while count < len(data):
        if data[count][0] == username:
            if encryption.verify(data[count][1], password):
                return data[count][2]
            else:
                return False
        else:
            count += 1
    print("User doesn't exist")


def user_add(name, password, key=encryption.key_gen()):
    file = open("userlist.txt", 'rb')
    data = pickle.load(file)
    file.close()
    for i in data:
        if i[0] == name:
            return False
    data.append((name, encryption.hasher(password), key))
    file = open('userlist.txt', 'wb')
    pickle.dump(data, file)
    file.close()
    file = open("data.txt", 'rb')
    data = pickle.load(file)
    file.close()
    data[name] = []
    file = open('data.txt', 'wb')
    pickle.dump(data, file)
    file.close()
    return True


def user_remove(username, password):
    if verify(username, password):
        file = open('userlist.txt', 'rb')
        data = pickle.load(file)
        file.close()
        count = 0
        while count < len(data):
            if data[count][0] == username:
                data.pop(count)
            count += 1
        file = open('userlist.txt', 'wb')
        pickle.dump(data, file)
        file.close()
        return True
    else:
        return False


def user_change(username, old_password, new_password):
    key = verify(username, old_password)
    if key != False:
        user_remove(username, old_password)
        user_add(username, new_password, key)
    else:
        return False

