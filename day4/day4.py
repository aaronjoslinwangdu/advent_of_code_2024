def main():
    g = [[c for c in ln] for ln in open("input.txt").read().split("\n")[:140]]
    m, n = len(g), len(g[0])

    # Part 1
    xmas = sum(
        all(
            0 <= i + di * k < m and 0 <= j + dj * k < n and ("X","M","A","S")[k] == g[i + di * k][j + dj * k]
            for k in range(4)
        )
        for i in range(m)
        for j in range(n)
        for di, dj in ((0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (1, -1), (-1, 1), (-1, -1))
    )
    print(f"XMAS Count: {xmas}") # Answer: 2336

    # Part 2
    cross = sum(
        0 < i < m - 1 and 0 < j < n - 1 and g[i][j] == "A" and {g[i - 1][j - 1], g[i + 1][j + 1]} == {"M","S"} and {g[i - 1][j + 1], g[i + 1][j - 1]} == {"M","S"}
        for i in range(m)
        for j in range(n)
    )
    print(f"X-MAS Count: {cross}")  # Answer: 1831

if __name__ == "__main__":
    main()
