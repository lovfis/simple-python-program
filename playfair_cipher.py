#One of the early common methods for encrypting text was the
#Playfair cipher. You can read more about the Playfair cipher
#here: https://en.wikipedia.org/wiki/Playfair_cipher
#
#The Playfair cipher starts with a 5x5 matrix of letters,
#such as this one:
#
# D A V I O
# Y N E R B
# C F G H K
# L M P Q S
# T U W X Z
#
#To fit the 26-letter alphabet into 25 letters, I and J are
#merged into one letter. When decrypting the message, it's
#relatively easy to tell from context whether a letter is
#meant to be an i or a j.
#
#To encrypt a message, we first remove all non-letters and
#convert the entire message to the same case. Then, we break
#the message into pairs. For example, imagine we wanted to
#encrypt the message "PS. Hello, worlds". First, we could
#convert it to PSHELLOWORLDS, and then break it into letter
#pairs: PS HE LL OW OR LD S. If there is an odd number of
#characters, we add X to the end.
#
#Then, for each pair of letters, we locate both letters in
#the cipher square. There are four possible orientations
#for the pair of letters: they could be in different rows
#and columns (the "rectangle" case), they could be in the
#same row but different columns (the "row" case), they could
#be in the same column but different rows (the "column"
#case), or they could be the same letter (the "same" case).
#
#Looking at the message PS HE LL OW OR LD SX:
#
# - PS is the Row case: P and S are in the same row.
# - HE is the Rectangle case: H and E are in different rows
#   and columns of the square.
# - LD is the Column case: L and D are in the same column.
# - LL is the Same case as it's two of the same letter.
#
#For the Same case, we replace the second letter in the pair
#with X, and then proceed as normal. When decrypting, it
#would be easy to see the our result was not intended to be
#PS HELXO WORLDSX, and we would thus assume the X is meant to
#repeat the previous letter, becoming PS HELLO WORLDSX.
#
#What we do for each of the other three cases is different:
#
# - For the Rectangle case, we replace each letter with
#   the letter in the same row, but the other letter's
#   column. For example, we would replace HE with GR:
#   G is in the same row as H but the same column as E,
#   and R is in the same row as E but the same column as
#   H. For another example, CS would become KL: K is in
#   C's row but S's column, and L is in C's column but S's
#   row.
# - For the Row case, we pick the letter to the right of
#   each letter, wrapping around the end of the row if we
#   need to. PS becomes QL: Q is to the right of P, and L
#   is to the right of S if we wrap around the end of the
#   row.
# - For the Column case, we pick the letter below each
#   letter, wrapping around if necessary. LD becomes TY:
#   T is below L and Y is below D.
#
#We would then return the resultant encrypted message.
#
#Decrypting a message is essentially the same process.
#You would use the exact same cipher and process, except
#for the Row and Column cases, you would shift left and up
#instead of right and down.
#
#Write two methods: encrypt and decrypt. encrypt should
#take as input a string, and return an encrypted version
#of it according to the rules above.
#
#To encrypt the string, you would:
#
# - Convert the string to uppercase.
# - Replace all Js with Is.
# - Remove all non-letter characters.
# - Add an X to the end if the length if odd.
# - Break the string into character pairs.
# - Replace the second letter of any same-character
#   pair with X (e.g. LL -> LX).
# - Encrypt it.
#
#decrypt should, in turn, take as input a string and
#return the unencrypted version, just undoing the last
#step. You don't need to worry about Js and Is, duplicate
#letters, or odd numbers of characters in decrypt.
#
#For example:
#
# encrypt("PS. Hello, world") -> "QLGRQTVZIBTYQZ"
# decrypt("QLGRQTVZIBTYQZ") -> "PSHELXOWORLDSX"
#
#HINT: You might find it easier if you implement some
#helper functions, like a find_letter function that
#returns the row and column of a letter in the cipher.
#
#HINT 2: Once you've written encrypt, decrypt should
#be trivial: try to think of how you can modify encrypt
#to serve as decrypt.
#
#To make this easier, we've gone ahead and created the
#cipher as a 2D tuple for you:
CIPHER = (("D", "A", "V", "I", "O"),
          ("Y", "N", "E", "R", "B"),
          ("C", "F", "G", "H", "K"),
          ("L", "M", "P", "Q", "S"),
          ("T", "U", "W", "X", "Z"))



#Add your code here!
#string library lets me use string.punctuation to take away punctuation
#from a string
import string

#function for finding the index of a letter n the 2D-CIPHER-tuple
def find_indexes_in_2D_list(myList, letter):
    for index, sub_list in enumerate(myList):
        if letter in sub_list:
            return (index, sub_list.index(letter))

def encrypt(message):
    
    #pairs_of_letters will hold a list of lists with paired letters to encrypt
    pairs_of_letters = []
    #make the string uppercase and remove blank spaces
    message = message.upper()
    message = message.replace(" ", "")
    #replace J with the letter I (only room for 25 letters in grid)    
    if "J" in message:
        message = message.replace("J", "I")
    #take away punctuation from the string
    for char in string.punctuation:
        message = message.replace(char, "")
    #add an ekstra letter(X) if the length of the string is odd
    if not len(message) % 2 == 0:
        message += "X"    
    #add letters from the string to the 2D list, two letters for each sublist
    for i in range(len(message)):
        if i % 2 == 1:
            pairs_of_letters.append([message[i-1], message[i]])      
    #Replace the second letter of any same-character pair with X      
    for i in range(len(pairs_of_letters)):
        if pairs_of_letters[i][0] == pairs_of_letters[i][1]:
            pairs_of_letters[i] = [pairs_of_letters[i][0], "X"]
            
    
    #empty message to store encrypted letters in while looping (look underneath)
    encrypted_message = ""
    
    #iterate through the list of pair of letters. Find their indexes in the CIPHER-grid.
    #Make new indexes according to the playfair-encryption-rules. Find new letters
    #in the CIPHER-grid using the new indexes. 
    for lst_num in range(len(pairs_of_letters)):
        
        sub_list = pairs_of_letters[lst_num]
        first = sub_list[0]
        second = sub_list[1]
        index_first_letter = find_indexes_in_2D_list(CIPHER, first)
        index_second_letter = find_indexes_in_2D_list(CIPHER, second)

        #check for letters in the same row and encrypt
        if index_first_letter[0] == index_second_letter[0]:
            #change indexes for first letter in pair
            if not index_first_letter[1] == 4:
                index_first_letter = (index_first_letter[0], index_first_letter[1] + 1)
            else:
                index_first_letter = (index_first_letter[0], 0)
            #change indexes for last letter in pair
            if not index_second_letter[1] == 4:
                index_second_letter = (index_second_letter[0], index_second_letter[1] + 1)
            else:
                index_second_letter = (index_first_letter[0], 0)
        
        #check for letters in the same column and encrypt
        elif index_first_letter[1] == index_second_letter[1]:
            #change indexes for first letter in pair
            if not index_first_letter[0] == 4:
                index_first_letter = (index_first_letter[0] + 1, index_first_letter[1])
            else:
                index_first_letter = (0, index_first_letter[1])
            #change indexes for last letter in pair
            if not index_second_letter[0] == 4:
                index_second_letter = (index_second_letter[0] + 1, index_second_letter[1])
            else:
                index_second_letter = (0, index_first_letter[1])       
            
        else:
            temp = index_first_letter[1]
            index_first_letter = (index_first_letter[0], index_second_letter[1])
            index_second_letter = (index_second_letter[0], temp)
            
        #print(index_first_letter, index_second_letter)
            
        #use the new indexes for the pair of letters to access new letters
        #in CIPHER-grid. Store new letters in encrypted_message.
        encrypted_first_letter_in_pair = CIPHER[index_first_letter[0]][index_first_letter[1]]
        encrypted_second_letter_in_pair = CIPHER[index_second_letter[0]][index_second_letter[1]]
        
        encrypted_message += (encrypted_first_letter_in_pair + \
        encrypted_second_letter_in_pair)
               
    return encrypted_message


    
def decrypt(code):
    
    #move all the letters in the code to a list if lists containing pairs of letters
    pairs_of_letters = []
    
    for i in range(len(code)):
        if i % 2 == 1:
            pairs_of_letters.append([code[i-1], code[i]])      

    #empty message to store decrypted letters in while looping (look underneath)
    decrypted_message = ""
    
    #iterate through the list of pair of letters. Find their indexes in the CIPHER-grid.
    #Make new indexes according to the playfair-decryption-rules. Find new letters
    #in the CIPHER-grid using the new indexes. 
    for lst_num in range(len(pairs_of_letters)):
        
        sub_list = pairs_of_letters[lst_num]
        first = sub_list[0]
        second = sub_list[1]
        index_first_letter = find_indexes_in_2D_list(CIPHER, first)
        index_second_letter = find_indexes_in_2D_list(CIPHER, second)

        #check for letters in the same row and encrypt
        if index_first_letter[0] == index_second_letter[0]:
            #change indexes for first letter in pair
            if not index_first_letter[1] == 0:
                index_first_letter = (index_first_letter[0], index_first_letter[1] - 1)
            else:
                index_first_letter = (index_first_letter[0], 4)
            #change indexes for last letter in pair
            if not index_second_letter[1] == 0:
                index_second_letter = (index_second_letter[0], index_second_letter[1] - 1)
            else:
                index_second_letter = (index_first_letter[0], 4)
        
        #check for letters in the same column and encrypt
        elif index_first_letter[1] == index_second_letter[1]:
            #change indexes for first letter in pair
            if not index_first_letter[0] == 0:
                index_first_letter = (index_first_letter[0] - 1, index_first_letter[1])
            else:
                index_first_letter = (4, index_first_letter[1])
            #change indexes for last letter in pair
            if not index_second_letter[0] == 0:
                index_second_letter = (index_second_letter[0] - 1, index_second_letter[1])
            else:
                index_second_letter = (4, index_first_letter[1])       
            
        else:
            temp = index_first_letter[1]
            index_first_letter = (index_first_letter[0], index_second_letter[1])
            index_second_letter = (index_second_letter[0], temp)
            
        #print(index_first_letter, index_second_letter)
            
        #use the new indexes for the pair of letters to access new letters
        #in CIPHER-grid (decrypt letters). Store new letters in decrypted_message.
        decrypted_first_letter_in_pair = CIPHER[index_first_letter[0]][index_first_letter[1]]
        decrypted_second_letter_in_pair = CIPHER[index_second_letter[0]][index_second_letter[1]]
        
        decrypted_message += (decrypted_first_letter_in_pair + \
        decrypted_second_letter_in_pair)
               
    return decrypted_message
              
            

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: QLGRQTVZIBTYQZ, then PSHELXOWORLDSX
print(encrypt("PS. Hello, worlds"))
print(decrypt("QLGRQTVZIBTYQZ"))

