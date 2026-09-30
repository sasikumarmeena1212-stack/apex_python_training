#FOR LOOP 

for i in range(1, 6):
    print(i)

    #WHILE LOOP
    i = 1

while i <= 5:
    print(i)
    i = i + 1

    #DO WHILE LOOP
    i = 1

while True:
    print(i)
    i = i + 1

    if i > 5:
        break

    #BREAK STATEMENT
    for i in range(1, 11):
    
        break
    print(i)


    #CONTINUE STATEMENT
    for i in range(1, 11):
    if i == 5:
        continue
    print(i)

    #BREAK AND CONTINUE COMBINED PROGRAM
    for i in range(1, 11):

    if i == 3:
        continue

    if i == 8:
        break

    print(i)
