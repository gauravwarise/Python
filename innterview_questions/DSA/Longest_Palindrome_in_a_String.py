s = 'abc'
count = 0
long_palindrom=s[0]
for i in range(len(s)):
    for j in range(i, len(s)+1):
        temp_s = s[i:j]
        if temp_s == (s[i:j])[::-1]:
            if len(long_palindrom)<len(temp_s):
                long_palindrom = temp_s
print(long_palindrom)
        # print((s[i:j])[::-1])

