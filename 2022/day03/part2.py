# oneliner!!
print(sum(list(map(lambda z: ord(z) - 96 if ord(z) > 96 else ord(z) - 38, list(map(lambda y: list((y[0] & y[1] & y[2]))[0], [list(map(lambda x: set(x.strip()), d[i:i+3])) for d in [open("input.txt", "r").readlines()] for i in range(0, len(d), 3)]))))))

# properly indented
print(
    sum(list(map(
            lambda z: ord(z) - 96 if ord(z) > 96 else ord(z) - 38,
            list(map(
            lambda y: list((y[0] & y[1] & y[2]))[0],
            [
            list(map(
                lambda x: set(x.strip()),
                d[i:i+3]))
            for d in [open("input.txt", "r").readlines()]  # tricky way to create a variable in a list comprehension
                for i in range(0, len(d), 3)
        ]))
    )))
)

