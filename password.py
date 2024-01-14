import string
import random
length = int(input("enter The length of Password:"))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
#symbols = 

all = lower + upper + num

temp = random.sample(all,length)

password = "".join(temp)

print("The Password Is:"+password)
