
# lambda agurment:expr
double=lambda x:x*2
print(double(3))

double=lambda x:x**3
print(double(2))

# filter function with lambda
num=[1,2,3,4,5,6,7,8,9,10]

new_list=list(filter(lambda x:(x%2==0),num))
print(new_list)

new_list=list(filter(lambda x:(x%2==0),num))
print(new_list)