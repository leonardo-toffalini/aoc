# oneliner!!
print(sum([a * c2.count(a) for c1, c2 in [[[x[i] for x in list(map(lambda x: list(map(int, x.strip().split("   "))), [d for d in open("input.txt", "r").readlines()]))] for i in range(2)]] for a in c1]))

# properly indented
print(
    sum([
        a * c2.count(a) for c1, c2 in
        [[
            [x[i] for x in list(map(
                lambda x: list(map(int, x.strip().split("   "))),
                [d for d in open("input.txt", "r").readlines()]
            ))]
            for i in range(2)
        ]]
        for a in c1
    ])
)
