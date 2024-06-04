package groupanagrams

import "sort"

type SortBy []rune

func (a SortBy) Len() int           { return len(a) }
func (a SortBy) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a SortBy) Less(i, j int) bool { return a[i] < a[j] }

func groupAnagrams(strs []string) [][]string {
	var result [][]string

	groupedAnagrams := make(map[string][]string)

	// iterate through the string on each iteration...
	for _, word := range strs {
		var key string
		var anagrams []string

		// ...sort the word
		key = sortWord(word)

		// ...check if the hashmap has the sorted word, if not then add a new entry with an empty []
		if _, ok := groupedAnagrams[key]; !ok {
			groupedAnagrams[key] = []string{}
		}

		// ...append the word to an array in the hashmap
		anagrams = groupedAnagrams[key]
		anagrams = append(anagrams, word)
		groupedAnagrams[key] = anagrams
	}

	// return an array of all the values within the hashmap
	for _, words := range groupedAnagrams {
		result = append(result, words)
	}

	return result
}

func sortWord(str string) string {
	s := []rune(str)
	sort.Sort(SortBy(s))
	return string(s)
}
