package main

import (
	"testing"
)

func TestDay3(t *testing.T) {
	input := []string{
		"00100",
		"11110",
		"10110",
		"10111",
		"10101",
		"01111",
		"00111",
		"11100",
		"10000",
		"11001",
		"00010",
		"01010",
	}

	result := day3Part2(input)

	expected := 230
	if result != expected {
		t.Errorf("Result was incorrect, got: %d, want: %d.", result, expected)
	}
}
