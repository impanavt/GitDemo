alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','']

def encryption(plain_text,shift_key):
    cipher_text=''
    for char in plain_text:
        position=alphabet.index(char)
        new_position=(position+shift_key)%26
        cipher_text+=alphabet[new_position]
    print(f'Here the text after encryption :{cipher_text}')

wanna_end=False
while not wanna_end:

    what_to_do=input("Type 'encrypt' for encryption ,type 'decryption:\n")
    text=input("Type your mesage:\n").lower()
    shift=int(input("Enter the shift key :\n"))
    if what_to_do=='encrypt':
        encryption(plain_text=text,shift_key=shift)
    elif what_to_do=='decrypt':
        decryption(text,shift)
    play_again=input("Type 'yes' to continue,type 'no' to exit.\n")
    if play_again=='no':
        wanna_end=True
        print('Have a nice day!')