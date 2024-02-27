arr = [6, -3, -10, 0, 2]
final_product=arr[0]
start_index = 0
end_index = 0
for i in range(len(arr)):
    temp_product =1
    for j in range(i,len(arr)):
        temp_product *= arr[j]
        if temp_product >final_product:
            final_product=temp_product
            start_index = i
            end_index = j
        

print(arr[start_index:end_index+1])
