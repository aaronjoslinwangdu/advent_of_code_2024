from bisect import bisect_left


def main():
    reports = parse_file('day2_input.txt')
    safe, safe_with_removal = get_safe_report_count(reports)
    print(f'Safe without removal: {safe}')
    print(f'Safe with removal: {safe_with_removal}')
    return

def parse_file(filename):
    reports = []
    for row in open(filename, 'r'):
        reports.append([int(val) for val in row.split(' ')])
    return reports

def get_safe_report_count(reports):
    safe, safe_with_removal = 0, 0
    for report in reports:
        safe += is_safe(report)
        safe_with_removal += is_safe_with_removal(report)
    return safe, safe_with_removal

# Part 1
def is_safe(report):
    inc, dec = True, True
    for i in range(1, len(report)):
        inc = inc and report[i - 1] < report[i] and report[i] - report[i - 1] < 4
        dec = dec and report[i - 1] > report[i] and report[i - 1] - report[i] < 4
    return inc or dec

# Part 2
def is_safe_with_removal(report):
    return any(is_safe(report[:i] + report[i + 1:]) for i in range(len(report)))

if __name__ == '__main__':
    main()