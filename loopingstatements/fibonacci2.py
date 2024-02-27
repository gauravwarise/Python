# a = 0
# b = 1

# n = 5


# print(f'{a}\n{b}')
# for i in range(1,n-1):
#     c = a + b
#     print(c)
#     a = b
#     b = c


# s = 'gaurav'
# reverse_string = ''
# for i in s:
#     reverse_string = i + reverse_string
# print(reverse_string)

# def reverse_array(array):
#     left = 0
#     right = len(array)-1
#     while left<right:
#         array[left], array[right] = array[right], array[left]
#         left += 1
#         right -= 1 
#     return array

# print(reverse_array([1,2,3,4,5]))


# def bubble_sort(array):
#     n = len(array)

#     for i in range(n):
#         for j in range(n-i-1):
#             if array[j]>array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#     return array


# print(bubble_sort([8,6,3,4,5,1]))




def plaindrom(num):
    for i in range(2, num):
        if num%i==0:
            return "prime"
        else:
            return 'not prime'

print(plaindrom(6))