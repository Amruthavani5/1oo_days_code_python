#indexing
name="amrutha"
print(name[0])#start index
print(name[-2])#negataive indexing

#string --->"amrutha"
#integer---> 1 2 3 ......
#primitive_data types
print(1+2)#integers
print(123_456_4)#large integers
print(1.2+3.4567)#float
print(True)#boolean --->False, True
print(type(True))# check data type--->type()

#type casting-->only valid litearals can be type casted----int(). str(), float(), bool()
num=int("1234")
print(type(num))

#operators (+,-,*,/,//, **) (5/3-->1.6666 (float)) (5//3-->1(int) (2**3--->8))
#PEMDASn(LR-->left to right) rule priority--->(), **, * , /, + , -
n=1.23456
print(round(n))#===>int(1.23456)
print(round(n,2))#-->round upto 2 digits

#compound operator(+=, -=, *=, /=
print(10%3)# modulo operator---->1(remainder)