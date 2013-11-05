

def primfac(n):
    """Makes a List of all prime factors of n."""

    F = []
    while n%2 == 0:
        F.append(2)
        n = n/2
    while n%3 == 0:
        F.append(3)
        n = n/3
    t = 5
    diff = 2
    while t*t <= n:
        while n%t == 0:
            F.append(t)
            n = n/t
        t = t + diff
        diff = 6 - diff
    if n > 1:
        F.append(n)
    return F

x = primfac(600851475143)
x.sort
print(x[-1])