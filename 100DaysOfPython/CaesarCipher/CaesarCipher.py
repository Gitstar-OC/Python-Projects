from CaesarCipherLogo import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def code(method, plain_text, shift_amount):
    Text = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        if method == "encode":
            newPosition = (position + shift_amount) % 26
            newLetter = alphabet[newPosition]
        elif method == "decode":
            newPosition = (position - shift_amount) % 26
            newLetter = alphabet[newPosition]
        else:
            print("Error! You typed something else.")
        Text += newLetter
    print(f"The {method}d text is {Text}")

code(method=direction, plain_text=text, shift_amount=shift)



#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#e.g.
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-listf

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# encrypt(plain_text=text, shift_amount=shift)

# def encrypt(plain_text, shift_amount):
#     encodedText = ''
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         newPosition = (position + shift_amount) % 26
#         newLetter = alphabet[newPosition]
#         encodedText += newLetter
#     print(f"The encoded text is {encodedText}")


#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.


#TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
#e.g.
#cipher_text = "mjqqt"
#shift = 5
#plain_text = "hello"
#print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that
# 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

# def decrypt(plain_text, shift_amount):
#     decodedText = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         newPosition = (position - shift_amount) % 26
#         newLetter = alphabet[newPosition]
#         decodedText += newLetter
#     print(f"The encoded text is {decodedText}")

# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(plain_text=text, shift_amount=shift)
# else:
#     print("Error! You have typed something else.")
