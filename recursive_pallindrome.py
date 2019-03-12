#PF-Assgn-40
def is_palindrome(word):
    if len(word)<=1:
        return True
    if(word[0].lower()!=word[len(word)-1].lower()):
        return False 
    else:
        return True and is_palindrome(word[1:len(word)-1])
    #Remove pass and write your logic here

#Provide different values for word and test your program
result=is_palindrome("Malayalam")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")