t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    k = 0
    while k < n and a[k] == 1:
        k += 1
    
    if k == n:
        # all ones
        if n % 2 == 1:
            print("First")
        else:
            print("Second")
    else:
        if k % 2 == 0:
            print("First")
        else:
            print("Second")
