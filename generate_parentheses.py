def generate_parentheses(n):
    results = []

    def open(pattern, opened, count):
        if count == 0:
            return
        else:
            pattern += "("
            opened += 1
            count -= 1
            open(pattern, opened, count)
            close(pattern, opened, count)

    def close(pattern, opened, count):
        if count == 0 and opened == 0:
            results.append(pattern)
        elif opened > 0:
            pattern += ")"
            opened -= 1
            open(pattern, opened, count)
            close(pattern, opened, count)

    pattern = "("
    open(pattern, 1, n - 1)
    close(pattern, 1, n - 1)

    print(results)

    return results

generate_parentheses(3)
