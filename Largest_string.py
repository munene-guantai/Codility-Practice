def lexicographically_largest_string(S):
    result = list(S)

    i = 0
    while i < len(result) - 1:
        while i < len(result) - 1 and int(result[i]) + int(result[i + 1]) > 9:
            i += 1

        if i < len(result) - 1:

            result[i] = str(int(result[i]) + int(result[i + 1]))
            result.pop(i + 1)

            i = max(0, i - 1)

    return ''.join(result)


print(lexicographically_largest_string("7531486"))
print(lexicographically_largest_string("246813579"))