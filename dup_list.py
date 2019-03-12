#PF-Assgn-44

def find_duplicates(list_of_numbers):
    dup_list=[]
    if(len(list_of_numbers)<2):
        return dup_list
    if list_of_numbers[0] in list_of_numbers[1:]:
        dup_list.append(list_of_numbers[0])
    temp=find_duplicates(list_of_numbers[1:])
    for item in temp:
        if not(item in dup_list):
            dup_list=dup_list+[item]
    return dup_list     
    #start writing your code here

list_of_numbers=[1,2,2,3,3,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)