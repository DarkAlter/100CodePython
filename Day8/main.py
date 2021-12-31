alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
sc= True
while sc == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift%26

    #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
    def encrypt(a,b):
        newText = ""
        for i in a:
            position = alphabet.index(i)
            new1 = position + b
            while(new1 > len(alphabet)):
                new1 = new1 - len(alphabet)
            newText += alphabet[new1]      
        print (newText)
        
    def decrypt(a,b):
        newText = ""
        for i in a:
            position = alphabet.index(i)
            new1 = position - b
            while(new1 < 0):
                new1 = new1 + len(alphabet)
            newText += alphabet[new1]   
        print (newText)
        
    if direction == "encode":
        encrypt(a=text, b=shift)
    else:
        decrypt(a=text, b=shift)
        #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
        #e.g. 
        #plain_text = "hello"
        #shift = 5
        #cipher_text = "mjqqt"
        #print output: "The encoded text is mjqqt"

        ##HINT: How do you get the index of an item in a list:
        #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

        ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

    #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
    shouldContinue = input("type 'yes' if you want to continue, otherwise type 'no' \n")
    if shouldContinue == "yes":
        sc = True
    else:
        sc = False