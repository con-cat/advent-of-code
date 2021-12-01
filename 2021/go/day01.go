package main

func day1(numbers []string) int {
	increaseCount := 0
	prevNumber := strToInt(numbers[0])
	for i, val := range numbers {
		if i > 0 {
			number := strToInt(val)
			if number > prevNumber {
				increaseCount++
			}
			prevNumber = number
		}
	}
	return increaseCount
}

type window struct {
	val1 int
	val2 int
	val3 int
}

func sumWindowVals(win window) int {
	return win.val1 + win.val2 + win.val3
}

func day1Part2(numbers []string) int {
	increaseCount := 0

	prevWindow := window{val1: strToInt(numbers[0]), val2: strToInt(numbers[1]), val3: strToInt(numbers[2])}

	for i, val := range numbers {
		if i > 2 {
			window := window{val1: strToInt(numbers[i-2]), val2: strToInt(numbers[i-1]), val3: strToInt(val)}
			if sumWindowVals(window) > sumWindowVals(prevWindow) {
				increaseCount++
			}
			prevWindow = window
		}
	}
	return increaseCount
}
