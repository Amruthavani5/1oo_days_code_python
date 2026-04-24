import random
random_integer=random.randint(1,10)
print(random_integer)
#random values from 0 to 1(float values btw 0 and 1)
random_num_0_to_1= random.random()
print(random_num_0_to_1)

#random float btw  range of values
random_float=random.uniform(1,10)
print(random_float)

#heads and tails
random_head_or_tail=random.randint(0,1)
if random_head_or_tail == 0:
    print("heads")
else:
    print("tails")