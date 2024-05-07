package validpalindrome

import "testing"

func TestIsPalindrome(t *testing.T) {
	var result bool

	if result = isPalindrome("A man, a plan, a canal: Panama"); result != true {
		t.Errorf("got %v, expected %v", result, true)
	}

	if result = isPalindrome("race a car"); result != false {
		t.Errorf("got %v, expected %v", result, false)
	}

	if result = isPalindrome(" "); result != true {
		t.Errorf("got %v, expected %v", result, true)
	}
}