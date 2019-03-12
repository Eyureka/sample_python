#PF-Assgn-41
def find_ten_substring(num_str):
    num_list=[]
    for i in range(0,len(num_str)-1):
        for j in range(i+1,len(num_str)):
            sum=0
            for k in range(i,j+1):
                sum+=int(num_str[k])
            if(sum==10):
                num_list.append(num_str[i:j+1])
    return num_list            
    #Remove pass and write your logic here

num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)