def computepay(h, rate):
    if h <= 40:
        ans = h * rate
        return ans
    else:
        diff = h - 40
        extra = rate * 1.5
        ans = 40 * rate
        ans += (diff * extra)
        return ans


hrs = input("Enter Hours:")
h = float(hrs)
r = float(input())
p = computepay(h, r)
print("Pay", p)
