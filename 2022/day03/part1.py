# oneliner!!
print(sum(list(map(lambda x: ord(x) - 96 if ord(x) > 96 else ord(x) - 38, [list(set(x[:len(x)//2]) & set(x[len(x)//2:]))[0] for x in open("input.txt", "r").readlines()]))))

# properly indented
print(
    sum(list(map(
        lambda x: ord(x) - 96 if ord(x) > 96 else ord(x) - 38,
        [
            list(
                set(x[:len(x)//2]) & set(x[len(x)//2:])
            )[0]
            for x in open("input.txt", "r").readlines()
        ]
    )))
)


