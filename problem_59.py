'''
Each character on a computer is assigned a unique code and the preferred 
standard is ASCII (American Standard Code for Information Interchange). 
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, 
then XOR each byte with a given value, taken from a secret key. The advantage 
with the XOR function is that using the same encryption key on the cipher text, 
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, 
and the key is made up of random bytes. The user would keep the encrypted message 
and the encryption key in different locations, and without both "halves", it is 
impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method 
is to use a password as a key. If the password is shorter than the message, which is 
likely, the key is repeated cyclically throughout the message. The balance for this 
method is using a sufficiently long password key for security, but short enough to be 
memorable.

Your task has been made easy, as the encryption key consists of three lower case 
characters. Using cipher.txt (right click and 'Save Link/Target As...'), a file 
containing the encrypted ASCII codes, and the knowledge that the plain text must 
contain common English words, decrypt the message and find the sum of the ASCII 
values in the original text.
'''

with open("problem_59_text.txt", "r") as f:
    lines = f.readlines()

def makeKey(password, message):
    password = [int(x) for x in password.split("-")]
    password_len = len(password)
    message_len = len(message)
    key = []
    j = 0
    for i in range(message_len):
        key.append(password[j])
        j += 1
        if j == password_len:
            j = 0

    return key

def numToChar(number):
    return chr(number)

data = lines[0].strip("\n")
chars = data.split(",")
chars = [int(x) for x in chars]

## 97 = 'a'
## 122 = 'z'

found = False
for a in range(97,123):
    if found:
        break
    for b in range(97,123):
        if found:
            break
        for c in range(97,123):
            password = "{}-{}-{}".format(a,b,c)
            this_key = makeKey(password, chars)
            res = [chars[i] ^ this_key[i] for i in range(len(chars))]
            res_string = "".join([numToChar(x) for x in res])
            common_words = ["the", "in", "a", "are", "is", "was"]
            logical = [x in res_string for x in common_words]
            if logical == [True]*len(common_words):
                found = True
                print("a = {}. b = {}, c = {}".format(a,b,c))
                print(res_string)
                break

print(sum(res))