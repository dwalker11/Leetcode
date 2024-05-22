package buyandsellstock

import "testing"

func TestMaxProfit(t *testing.T) {
	var (
		profit int
		target int
		prices []int
	)

	prices = []int{7,1,5,3,6,4}
	target = 5
	if profit = maxProfit(prices); profit != target {
		t.Errorf("Expected %v: got %v", target, profit)
	}

	prices = []int{7,6,4,3,1}
	target = 0
	if profit = maxProfit(prices); profit != target {
		t.Errorf("Expected %v: got %v", target, profit)
	}

	prices = []int{4,2,1,7}
	target = 6
	if profit = maxProfit(prices); profit != target {
		t.Errorf("Expected %v: got %v", target, profit)
	}
}