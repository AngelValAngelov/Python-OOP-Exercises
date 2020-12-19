def solve(index, n):
    length = ' ' * (n - index - 1)
    stars = '* ' * (index + 1)
    return f'{length}{stars}'


def rhombus(n):
    for i in range(n):
        print(solve(i, n))

    for i in range(n - 2, -1, -1):
        print(solve(i, n))


rhombus(int(input()))

