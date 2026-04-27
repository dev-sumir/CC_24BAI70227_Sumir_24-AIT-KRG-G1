import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    if min(n, m) % 2 != 0:
        print("Akshat")
    else:
        print("Malvika")

if __name__ == "__main__":
    solve()
