# we define functions with whitespace and the def keyword

# define a double function for a list of variables passed by value
def mult_2(x):
    return (x*2)
y = mult_2(12)
print(y)

# define a double function for a list of variables passed by reference

def mult_2_list(l):
    for el in range(len(l)):
        l[el] *= 2

nums = [1,2,3,4]
print(nums)
mult_2_list(nums)
print(nums)