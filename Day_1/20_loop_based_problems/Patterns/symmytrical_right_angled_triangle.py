def symmetrical_right_angled_triangle(n):
    space = 2*(n-1)
    for i in range(n):
        for j in range(i+1):
            print(j+1, end=' ')
        for j in range(space):
            print(" ", end=' ')
        for j in range(i+1, 0, -1):
           print(j, end=' ')

        print()
        space -= 2
symmetrical_right_angled_triangle(15)