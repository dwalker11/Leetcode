package stringencodedecode

import (
	"fmt"
	"strconv"
)

func encode(strs []string) string {
	var output string

	for _, s := range strs {
		output += fmt.Sprintf("%d:%s", len(s), s)
	}

	return output
}

func decode(str string) []string {
	var output []string

	s := 0
	for s < len(str) {
		e := s

		for str[e] != ':' {
			e++
		}

		wordLength, _ := strconv.Atoi(str[s:e])
		s = e + 1
		e = s + wordLength 

		output = append(output, str[s:e])
		s = e
	}

	return output
}
