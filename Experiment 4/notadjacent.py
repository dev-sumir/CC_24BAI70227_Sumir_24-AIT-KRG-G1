import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        
        if n == 1:
            print(1)
            continue
        if n == 2:
            print(-1)
            continue
        
        nums = []
        for i in range(1, n*n + 1, 2):
            nums.append(i)
        for i in range(2, n*n + 1, 2):
            nums.append(i)
            
        for i in range(n):
            print(*(nums[i*n : (i+1)*n]))

if __name__ == "__main__":
    solve()
