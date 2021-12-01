package main

import (
	"testing"
)

func TestDay1(t *testing.T) {
	input := []string{
		"199",
		"200",
		"208",
		"210",
		"200",
		"207",
		"240",
		"269",
		"260",
		"263",
	}

	// Part 1
	result := day1(input)

	expected := 7
	if result != expected {
		t.Errorf("Result was incorrect, got: %d, want: %d.", result, expected)
	}

	// Part 2
	result = day1Part2(input)

	expected = 5
	if result != expected {
		t.Errorf("Result was incorrect, got: %d, want: %d.", result, expected)
	}
}
