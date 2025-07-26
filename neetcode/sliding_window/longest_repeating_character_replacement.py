def characterReplacement(s: str, k: int) -> int:
    results = 0
    selected_char = s[0]
    remaining_replacements = k

    l = 0
    for r in range(0, len(s)):
        if s[r] == selected_char or remaining_replacements > 0:
            if s[r] != selected_char:
                remaining_replacements -= 1
            r += 1
        else:
            results = max(results, len(s[l:r]))
            selected_char = s[r]
            remaining_replacements = k

            for i in range(r, -1, -1):
                prev = s[i]

                if prev != selected_char and remaining_replacements < 1:
                    break

                if prev != selected_char:
                    remaining_replacements -= 1

                l = i

            r += 1

    return max(results, len(s[l:r]))


results = characterReplacement("ABBB", 1)
print(f"Expected 4 got {results}")

results = characterReplacement("AABABBA", 1)
print(f"Expected 4 got {results}")

results = characterReplacement("ABAB", 2)
print(f"Expected 4 got {results}")
