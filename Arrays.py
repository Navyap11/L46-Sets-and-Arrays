import array as ray

A_num= ray.array("i", [2,3,4,5,5,4,3,2,3])
print("OG array: "+str(A_num))

print("Amount of times 3 has been listed in the numbers above: "+str(A_num.count(3)))

A_num.reverse()
print("The reversed version of the listed numbers above is: "+str(A_num))