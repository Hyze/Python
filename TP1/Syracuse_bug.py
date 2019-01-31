



def calcul(var):
    n= int(var)
    if(n>0):
        value = [n]

        if(n > 1):

            max = n

            count = 1



            while (n > 1):

                if (n % 2 == 0):

                    n = n / 2

                else:

                    n = 3 *n + 1
                value.append(n)
                count = count + 1

            if (n > max):
                max = n

                print(n)


            print("nombre de termes dans la suite :" + str(count))

            print("valeur max de la suite :" + str(max))
            print(value);

    elif(n<=0):
                print("Le nombre rentré doit etre supérieur a 0")
