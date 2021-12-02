package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func sliceFileLines(filePath string) []string {
	file, err := os.Open(filePath)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	sc := bufio.NewScanner(file)
	lines := make([]string, 0)

	// Read through 'tokens' until an EOF is encountered.
	for sc.Scan() {
		lines = append(lines, sc.Text())
	}

	if err := sc.Err(); err != nil {
		log.Fatal(err)
	}

	return lines
}

func strToInt(str string) int {
	integer, err := strconv.Atoi(str)
	if err != nil {
		log.Fatal(err)
	}
	return integer
}

func main() {
	fmt.Println("=== Day 2 ===")
	input := sliceFileLines("../input/day02.txt")

	result := day2(input)
	fmt.Printf("Part 2 result: %d\n", result)
}
