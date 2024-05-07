package validpalindrome

import (
	"regexp"
	"strings"
)

func isPalindrome(s string) bool {
	re := regexp.MustCompile(`[a-zA-Z0-9]`)
	x := re.FindAllString(s, -1)
	y := strings.Join(x, "")
	z := strings.ToLower(y)

	var i, j = 0, len(z) - 1

	for i < j {
		if z[i] != z[j] {
			return false
		}

		i++
		j--
	}

	return true
}
