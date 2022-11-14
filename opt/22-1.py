import sys
fileName = sys.argv[1]
line_count = 0
with open(fileName) as f:
    for line in f:
        line_count += 1

print(line_count)