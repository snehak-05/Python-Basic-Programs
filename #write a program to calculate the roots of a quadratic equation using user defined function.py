def quadraticsolver():
    a = float(input('Enter value of a = '))
    b = float(input('Enter value of b = '))
    c = float(input('Enter value of c = '))
    import math
    discriminant = b**2 - 4*a*c
    if discriminant == 0:
            roots = 'There is one real root'
            root1 = (-b + math.sqrt((b**2 - 4*a*c))) / 2*a
            print(roots)
            print('x = ' + str(round(root1,2)))
    elif discriminant > 0:
            roots = 'There are two real roots'
            root1 = (-b + math.sqrt((b**2 - 4*a*c))) / 2*a
            root2 = (-b - math.sqrt((b**2 - 4*a*c))) / 2*a
            print(roots)
            print('x = ' + str(round(root1,2)) + ' or ' + str(round(root2,2)))
    elif discriminant < 0:
            roots = 'There are no real roots'
            print(roots)
quadraticsolver()
