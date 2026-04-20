#Task 2[mradul]: List Analysis + File Write
#List: [10, 15, 20, 25]
#Separate even/odd.
#Compute sum and max.
#Write into output.txt.
# Read and display.

num=[10,15,20,25]
even=[]
odd=[]
for i in num:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
sum=0
maximum=num[0]
for i in num:
    sum=sum+i
    if i>maximum:
        maximum=i
print(f"The maximum number is :{maximum}")
        
print(f"The sum of numbers is : {sum}")

#To write the output in the  file
f=open("Week_1/output.txt","w")
f.write("The sum of numbers is "+str(sum))
f.write("\nThe maximum number is "+str(maximum))
f.close()

#To read the file and display
f=open("Week_1/output.txt","r")
print(f.read())
f.close()

    
            

