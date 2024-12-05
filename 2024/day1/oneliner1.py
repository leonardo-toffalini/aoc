# oneliner!!
print(sum([abs(a - b) for a, b in zip(*list(map(sorted, [[x[i] for x in list(map(lambda x: list(map(int, x.strip().split("   "))), [d for d in open("input.txt", "r").readlines()]))] for i in range(2)])))]))

# properly indented
print(
    sum([
        abs(a - b) for a, b in
        zip(*list(map(
            sorted,
            [
                [x[i] for x in list(map(
                    lambda x: list(map(int, x.strip().split("   "))),
                    [d for d in open("input.txt", "r").readlines()]
                ))]
                for i in range(2)
            ]
        )))
    ])
)
