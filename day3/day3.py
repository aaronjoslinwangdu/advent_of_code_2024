import re

def main():
    # Part 1
    total_sum = sum(
        int(x) * int(y)
        for x, y in re.findall(r"mul\((\d+),(\d+)\)", open("input.txt").read())
    )
    print(f"Total sum: {total_sum}")

    # Part 2
    do_sum, do = 0, True
    for match in re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", open("input.txt").read()):
        m, x, y = match.group(0, 1, 2)
        if m == "do()":
            do = True
        elif m == "don't()":
            do = False
        elif do:
            do_sum += int(x) * int(y)
    print(f"Do sum: {do_sum}")

if __name__ == "__main__":
    main()