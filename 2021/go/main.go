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
	// 1 December
	fmt.Println("=== Day 1 ===")
	input := sliceFileLines("../input/day01.txt")
	increaseCount := day1Part2(input)
	fmt.Println(increaseCount)
}
