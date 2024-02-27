n=5
s=12
arr = [1,2,3,7,5]
final_sum=0
temp_sum=0
for i in range(len(arr)):
    for j in range(i,len(arr)+1):
        temp_sum =sum(arr[i:j])
        array = arr[i:j]
        if temp_sum==12:
            final_sum=temp_sum
            print("output",i,j)
            print(array)

print(final_sum)
