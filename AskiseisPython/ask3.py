alphabet='abcdefghijklmnopqrstuvwxyz'
newmessage=''
message=input('Please enter a message:')
for character in message:
  if character in alphabet:
    position=alphabet.find(character)
    newposition=(position+13)%26
    newcharacter=alphabet[newposition]
    newmessage+=newcharacter
  else:
    newmessage+=character
  
  

  
  








print('Your new message is:',newmessage)