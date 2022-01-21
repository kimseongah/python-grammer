inp = input()
result = int(inp[0])
for x in inp[1:]:
    if x == 0 or result == 0:
        result += int(x)
    else:
        result *= int(x)

print(result)