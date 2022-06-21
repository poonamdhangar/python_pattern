"""
                    *
                   ***
                  *****
                 *******
                *********
"""


# rows = int(input("Enter number of rows: "))

# k = 0

# for i in range(1, rows+1):
#     for space in range(1, (rows-i)+1):
#         print(end="  ")
   
#     while k!=(2*i-1):
#         print("* ", end="")
#         k += 1
   
#     k = 0
#     print()
k=0
for i in range(1,6):
    for j in range(1,(6-i)+1):
        print(end="1")
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()

