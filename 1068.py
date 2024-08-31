num1 = int(input())
saida = str(num1)

while True:

    if num1 != 1:

        if num1 % 2 == 0:

            num1 = num1 / 2

        else:
            num1 = num1 * 3 + 1

        saida += ' ' + str(int(num1))    


    elif num1 == 1: break

print(saida)
