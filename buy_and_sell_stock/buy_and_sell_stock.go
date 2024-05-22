package buyandsellstock

func maxProfit(prices []int) int {
	if len(prices) < 2 {
		return 0
	}

	s, e := 0, 1
	profit := prices[e] - prices[s]

	lowest := s
	if prices[e] < prices[lowest] {
		lowest = e
	}

	for i := e + 1; i < len(prices); i++ {
		newProfit := prices[i] - prices[lowest]

		if newProfit > profit {
			e = i
			s = lowest
			profit = newProfit
		}

		if prices[i] < prices[lowest] {
			lowest = i
		}
	}

	if profit < 0 {
		return 0
	}

	return profit
}
