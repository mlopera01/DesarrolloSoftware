#La regla principal que da origen al triángulo tiene que ver con la longitud
#de sus lados. Esta plantea que la suma de dos de sus lados debe ser mayor
#a la longitud del tercer lado. Por ejemplo, si dos lados miden cinco y cuatro
#centímetros respectivamente, el tercero lado debería medir ocho centímetros.

def check_triangle(sides):

    a = sides[0]
    b = sides[1]
    c = sides[2]
    #if(((a+b)> c)or((b+c)>a)or((a+c)>b)):
    if((a+b)>c) and (b<(a+c)):
        print("Si es un triangulo")
        type_triangle(a,b,c)
    else:
        print("No es un triangulo")

def type_triangle(a,b,c):              
    if (a==b==c):
        print('Es un triángulo equilátero')
    elif ((a==b)or(b==c)or(a==c)):
        print('Es un triángulo Isósceles')
    else:
        print('Es un triángulo Escaleno')

def main():
    result=0
    sides=[0,0,0]
    sides[0] = int(input("Ingresa lado a \n" ))
    sides[1] = int(input("Ingresa lado b\n" ))
    sides[2] = int(input("Ingresa lado c\n" ))

    check_triangle(sides)
   
if __name__ == "__main__":

    main()

