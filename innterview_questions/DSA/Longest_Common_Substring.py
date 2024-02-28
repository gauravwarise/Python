s1 = 'ABC'
s2 = 'ACB'
n = len(s1)
m = len(s2)
longest_substring=str()
# print(len(longest_substring))
for i in range(n):
    for j in range(i,n+1):
        substring = s1[i:j]
        if substring in s2:
            if len(substring)>len(longest_substring):
                longest_substring=substring

print(len(longest_substring), longest_substring)
            


