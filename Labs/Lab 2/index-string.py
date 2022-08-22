greeting = "Hello, World!"

print(greeting[0])
print(greeting[1])
print(greeting[2])
print(greeting[-1])

for j in range(5):
    print(greeting[j])
    
for j in range(len(greeting)):
    print(greeting[j])   
    
for j in range(0,10,2):
    print(greeting[j])  
    
for j in range(10,0,-1):
    print(greeting[j])