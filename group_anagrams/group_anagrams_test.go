package groupanagrams

import (
	"fmt"
	"testing"
)

func TestGroupAnagrams(t *testing.T) {
	var result [][]string

	input := []string{""}
	result = groupAnagrams(input)
	printList(result)
	
	input2 := []string{"a"}
	result = groupAnagrams(input2)
	printList(result)
	
	input3 := []string{"eat", "tea", "tan", "ate", "nat", "bat"}
	result = groupAnagrams(input3)
	printList(result)
}

func printList(x [][]string) {
	for _, v := range x {
		fmt.Print(v)
	}
	fmt.Println()
}