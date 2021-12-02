package main

import (
	"log"
	"strings"
)

func day2(input []string) int {
	horizontalPos := 0
	depth := 0
	aim := 0
	for _, value := range input {
		// Get the direction and distance
		split := strings.Split(value, " ")
		if len(split) != 2 {
			log.Fatalf("Can't parse direction %s", value)
		}
		direction := split[0]
		distance := strToInt(split[1])

		switch direction {
		case "forward":
			horizontalPos += distance
			depth += aim * distance
		case "down":
			aim += distance
		case "up":
			aim -= distance
		}
	}
	return horizontalPos * depth
}
