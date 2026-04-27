import sys

def solve():
    line1 = sys.stdin.readline()
    if not line1:
        return
    n = int(line1)
    
    line2 = sys.stdin.readline()
    if not line2:
        return
    a = list(map(int, line2.split()))
    
    total_ones = sum(a)
    max_gain = -float('inf')
    current_gain = 0
    
    for x in a:
        val = 1 if x == 0 else -1
        current_gain += val
        
        if current_gain > max_gain:
            max_gain = current_gain
        
        if current_gain < 0:
            current_gain = 0
            
    print(total_ones + max_gain)

if __name__ == "__main__":
    solve()
