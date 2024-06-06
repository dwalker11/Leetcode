package stringencodedecode

import (
	"fmt"
	"slices"
	"testing"
)

func TestEncode(t *testing.T)  {
	var input, output []string

	input = []string{"neet", "code", "love", "you"}

	encodedStr := encode(input)
	fmt.Println(encodedStr)

	output = decode(encodedStr)
	fmt.Println(output)

	if slices.Compare(input, output) != 0 {
		t.Errorf("Error: input and output don't match")
	}

	input = []string{"we", "say", ":", "yes"}

	encodedStr2 := encode(input)
	fmt.Println(encodedStr2)

	output = decode(encodedStr2)
	fmt.Println(output)

	if slices.Compare(input, output) != 0 {
		t.Errorf("Error: input and output don't match")
	}
}