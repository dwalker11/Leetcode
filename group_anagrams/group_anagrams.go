package groupanagrams

// import "sort"

type alphabetArr [26]rune

type SortBy []rune

func (a SortBy) Len() int           { return len(a) }
func (a SortBy) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a SortBy) Less(i, j int) bool { return a[i] < a[j] }

// func sortWord(str string) string {
// 	s := []rune(str)
// 	sort.Sort(SortBy(s))
// 	return string(s)
// }

func groupAnagrams(strs []string) [][]string {
	var result [][]string

	// groupedAnagrams := make(map[string][]string)
	groupedAnagrams := make(map[alphabetArr][]string)

	for _, word := range strs {
		var key alphabetArr
		var anagrams []string

		key = getKey(word)

		if _, ok := groupedAnagrams[key]; !ok {
			groupedAnagrams[key] = []string{}
		}

		anagrams = groupedAnagrams[key]
		anagrams = append(anagrams, word)
		groupedAnagrams[key] = anagrams
	}

	for _, words := range groupedAnagrams {
		result = append(result, words)
	}

	return result
}

func getKey(word string) alphabetArr {
	key := alphabetArr{}
	for _, c := range word {
		i := c - 'a'
		key[i] += 1
	}
	return key
}
