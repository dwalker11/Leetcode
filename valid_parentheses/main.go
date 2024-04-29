package main

import (
	"errors"
	"fmt"
)

// Set data structure
type Set struct {
	Elements map[rune]struct{}
}

func NewSet() *Set {
	s := Set{Elements: map[rune]struct{}{}}
	return &s
}

func (s *Set) Add(elem rune) {
	s.Elements[elem] = struct{}{}
}

func (s *Set) Has(elem rune) bool {
	_, exists := s.Elements[elem]
	return exists
}

// Stack data structure
type Stack struct {
	Elements []rune
	Top      int
}

func NewStack() *Stack {
	s := Stack{Elements: []rune{}, Top: -1}
	return &s
}

func (s *Stack) Push(elem rune) {
	s.Elements = append(s.Elements, elem)
	s.Top++
}

func (s *Stack) Pop() rune {
	// if s.IsEmpty() {
	// 	return 0, errors.New("The stack is empty")
	// }
	result := s.Elements[s.Top]
	s.Elements = s.Elements[:s.Top]
	s.Top--
	return result
}

func (s Stack) Peek() (rune, error) {
	if s.IsEmpty() {
		return 0, errors.New("The stack is empty")
	}
	return s.Elements[s.Top], nil
}

func (s Stack) IsEmpty() bool {
	return len(s.Elements) == 0
}

func main() {
	fmt.Println(isValid("()[]}{"))
}

func isValid(s string) bool {
	charSet := NewSet()
	charSet.Add('{')
	charSet.Add('[')
	charSet.Add('(')

	charStack := NewStack()
	charStack.Push(rune(s[0]))

	for _, c := range s[1:] {
		if charSet.Has(c) {
			charStack.Push(c)
		} else if topChar, err := charStack.Peek(); err == nil && isMatch(topChar, c) {
			charStack.Pop()
		} else {
			return false
		}
	}

	if !charStack.IsEmpty() {
		return false
	}

	return true
}

func isMatch(target rune, value rune) bool {
	switch target {
	case '{':
		return value == '}'
	case '[':
		return value == ']'
	case '(':
		return value == ')'
	default:
		return false
	}
}
