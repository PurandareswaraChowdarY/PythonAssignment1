#Square root of a number without using sqrt() function in Python

def findSqrt(x):
    # for 0 and 1, the square roots are themselves
    if x < 2:
        return x

    # considering the equation values
    y = x
    z = (y + (x / y)) / 2

    # as we want to get upto 5 decimal digits, the absolute difference should not exceed
    # 0.00001
    while abs(y - z) >= 0.00001:
        y = z
        z = (y + (x / y)) / 2

    return z


if __name__ == '__main__':
    n = 346535

    ans = findSqrt(n)
    print(ans)