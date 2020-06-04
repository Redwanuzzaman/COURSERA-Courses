hrs = input("Enter Hours:")
h = float(hrs)
rate = float(input())

if h <= 40:
    ans = h * rate
    print(ans)
else:
    diff = h - 40
    extra = rate * 1.5
    ans = 40 * rate
    ans += (diff * extra)
    print(ans)
