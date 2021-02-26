alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ','1','2','3','4','5','6','7','8','9','0','$','!','#','@','%','^','&','*','(',')','-','_','=','<','>','/','?','.',',']
import art
print(art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
# function for encoding & decoding
def caesar(message,shifting_no,position):
  code = ''
  for char in message:
    indexing = alphabet.index(char)
    if position == 'encode':
      indexing = indexing + shifting_no
    else:
      indexing = indexing - shifting_no
    indexing = indexing % 56
    string = alphabet[indexing]
    code += string
  print(f'The {position}d text is {code}')
caesar(text,shift,direction)
endGame = True
while endGame:
  restart = input("Type 'yes' to play again.Otherwise type 'no': ").lower()
  if restart == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)
  else:
    print('GameOver')
    endGame = False
  
