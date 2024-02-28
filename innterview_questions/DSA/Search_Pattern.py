txt = "abesdu"
pat = "geek"
index_list = []
for i in range(len(txt)):
    for j in range(i,len(txt)+1):
        tem_str = txt[i:j]
        if pat==tem_str:
            index_list.append(i+1)
if index_list:
    for i in index_list:
        print(i,end=' ')
else:
    print(-1)
# print(index_list)