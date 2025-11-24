def reverse(n):
    for i in range(n):
        for j in range(n-i):
            print("*", end=' ')
        print()
reverse(5)