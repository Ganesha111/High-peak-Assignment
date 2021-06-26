from os import close, write


file1=open(r"C:\Users\Ṅ\Desktop\high peak assignment\input.txt","r") 
lines = file1.readlines()
goodies=[]
number_of_employees=int(lines[0][-2])
for i in range(4,len(lines)):
    L=lines[i].split(":")
    goodies.append([L[0],int(L[1])])
goodies1=sorted(goodies,key=lambda x:x[1])
min_diff=float('inf')
for i in range(0,len(goodies1)-number_of_employees+1):
    diff=goodies1[i+number_of_employees-1][1]-goodies1[i][1]
    if diff<min_diff:
        min_index=i
        min_diff=diff
file1.close()
file2=open(r"C:\Users\Ṅ\Desktop\high peak assignment\output.txt","w")
file2.write("the goodies selected for distribution are:\n")
file2.write("\n")
for i in range(min_index,min_index+number_of_employees):
    print(goodies1,file=file2)
    break
file2.write("lowest price is : ")
print(min_diff,file=file2)
file2.close()