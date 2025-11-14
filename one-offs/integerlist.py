import random


for i in range(10000):
    # if we put out a list like 1,2,3,4, turn_array fails because of last comma
    temp_string = ''.join(map(lambda x: str(x)+"," ,[random.randint(-10,10) for _ in range(10)])) 
    # cheap chomp [:-1] , also ::-1 is a flip string
    print(temp_string[:-1] )
