import sys

def solve():
    line1 = sys.stdin.readline().split()
    if not line1:
        return
    n, t = map(int, line1)
    
    line2 = sys.stdin.readline().split()
    if not line2:
        return
    a = list(map(int, line2))
    
    max_books = 0
    current_time = 0
    left = 0
    
    for right in range(n):
        current_time += a[right]
        
        while current_time > t:
            current_time -= a[left]
            left += 1
            
        max_books = max(max_books, right - left + 1)
        
    print(max_books)

if __name__ == "__main__":
    solve()
