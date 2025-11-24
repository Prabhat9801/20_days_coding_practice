def right_angled_triangle(n):
    i = 0
    for i in range(n):
        for j in range(i+1):
            print("*", end=' ')
        print()
right_angled_triangle(5)