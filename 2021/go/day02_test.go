package main

import (
	"testing"
)

func TestDay2(t *testing.T) {
	input := []string{
		"forward 5",
		"down 5",
		"forward 8",
		"up 3",
		"down 8",
		"forward 2",
	}

	// Part 2
	result := day2(input)

	expected := 900
	if result != expected {
		t.Errorf("Result was incorrect, got: %d, want: %d.", result, expected)
	}
}
