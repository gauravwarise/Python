l = [1,3,2,4,5,6,3,1]
for index, num in enumerate(l):
    print(index, num)


# largest number from list
max_sum = l[0]
for i in range(1,len(l)):
    if l[i]>max_sum:
        max_sum = l[i]
    else:
        pass
print(max_sum)

# sort a list 
for i in range(len(l)):
    for j in range(len(l)-1):
        if l[j]>l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]

print(l)


# reverse a list 
start = 0
end = len(l)-1

while start<end:
    l[start], l[end] = l[end], l[start]
    start += 1
    end -= 1

print(l)


# array =  [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# max_sum = array[0]
# current = array[0]

# for i in array[1:]:
#     current = max(num, current+num)
#     max_sum = max(max_sum, current)

# print(max_sum)


def max_subarray_sum(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum 

# Example usage
arr = [1,2,3,7,5]
sum_of_element = 0
current_element_sum = 0
array = []
for i in range(len(arr)):
    for j in range(i,len(arr)+1):
        current_element_sum = sum(arr[i:j])
        if current_element_sum>sum_of_element:
            array = arr[i:j]
            sum_of_element=current_element_sum
print(sum_of_element, array)
    #     current_element_sum = current_element_sum + arr[j]
    #     print(f"{arr[i]}+{arr[j]} {arr[i] + arr[j]} ==== {current_element_sum>sum_of_element}")
    # if current_element_sum>sum_of_element:
    #     sum_of_element = current_element_sum
    # else:
    #     pass

# print(sum_of_element)