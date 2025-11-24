def right_angled_triangle_in_numbers(n):
    i = 1
    for i in range(n):
        for j in range(i+1):
            print(j+1, end=' ')
        print()
right_angled_triangle_in_numbers(5)