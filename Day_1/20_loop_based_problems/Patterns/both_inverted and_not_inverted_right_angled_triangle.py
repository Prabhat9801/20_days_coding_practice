def both_triangles(n):
    for i in range(2*n-1):
        for j in range(i+1):
            if i<n:
                if j<=i:
                    print("*", end=' ')
            else:
                if j<2*n-1-i:
                    print("*", end=' ')
        print()
both_triangles(5)