import nacl.exceptions
import nacl.secret
import nacl.utils
import nacl.pwhash


def key_gen():
    #generates random key
    key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
    return key


def encrypter(msg, key):
    #It takes bytes object and encrypts it using the key
    #and returns an encrypted message in the form of bytes object
    box = nacl.secret.SecretBox(key)
    encrypted = box.encrypt(msg)
    return encrypted


def decrypter(encrypted, key):

    try:
        box = nacl.secret.SecretBox(key)
        decrypted = box.decrypt(encrypted)
        return decrypted
    except nacl.exceptions.CryptoError:
        return False


def hasher(x):
    '''It takes str input and returns hashed output
    It gives bytes object as an output'''
    k = bytes(x, 'ASCII')
    return nacl.pwhash.scrypt.str(k)


def verify(hashed, password):
    """It takes bytes input for both
	hashed and password
	and verify original hashed function and given password.
	It gives boolean output"""
    psd = bytes(password, 'ASCII')
    try:
        res = nacl.pwhash.verify(hashed, psd)
    except nacl.exceptions.InvalidkeyError:
        res = False
    return res
