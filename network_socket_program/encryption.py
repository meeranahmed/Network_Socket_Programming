from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random
import binascii
import base64


def encrypt(key, text):
    """ Returns encrypted cipher using AES-256 encryption ctr mode """
    #check key size
    check_key(key)

    #create a random 16-byte IV
    iv_bytes = Random.new().read(AES.block_size)

    #convert the IV to integer
    iv = int(binascii.hexlify(iv_bytes), 16) 

    #create a new Counter object
    ctr = Counter.new(AES.block_size * 8, initial_value=iv)

    #create AES-CTR cipher
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)

    #Encrypt and return IV and encoded cipher
    cipher = aes.encrypt(text.encode('utf-8')) 
    print(type(cipher))
    return base64.b64encode(iv_bytes+ cipher)



def decrypt(key, cipher):
    """ Return decrypt cipher from AES-256 ctr encryption"""

    #check key size
    check_key(key)
    
    #Decode cipher
    cipher = base64.b64decode(cipher)
    
    #extract iv from cipher
    iv_bytes= cipher[:16]
    iv = int(binascii.hexlify(iv_bytes), 16)

    #create a new Counter object
    ctr = Counter.new(AES.block_size * 8, initial_value=iv)

    #create AES-CTR cipher
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)

    # Decrypt and return the plaintext.
    text = aes.decrypt(cipher[16:])

    return text


#check for 32-byte key    
def check_key(key):
    assert len(key) == 32
