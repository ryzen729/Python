alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.



def encrypt(text,shift):
  text_list = list()
  for i in text:
    text_list.append(i)
  print(text_list)
  
  
  encode_list = list()
  for i in text_list:
    index = 0
    new_index = 0
    for j in alphabet:
      if i == j:
        new_index = index + shift
        if new_index >= 25:
          remain_index = new_index - 25
          new_index = remain_index -1
        encode_list.append(alphabet[new_index])
      index += 1
  print(encode_list)
  
     


def decrypt(text,shift):
  text_list = list()
  for i in text:
    text_list.append(i)
  print(text_list)
  
  
  decode_list = list()
  for i in text_list:
    index = 0
    new_index = 0
    for j in alphabet:
      if i == j:
        new_index = index - shift
        if new_index <= 0:
          remain_index = new_index - 25
        decode_list.append(alphabet[new_index])
      index += 1
  print(decode_list)

     
        
if direction == "encode":
    encrypt(text,shift)
elif direction == "decode":
    decrypt(text,shift)