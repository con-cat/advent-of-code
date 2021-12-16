package main

import (
	"log"
	"strconv"
)

func bitStrToInt(str string) int64 {
	integer, err := strconv.ParseInt(str, 2, 64)
	if err != nil {
		log.Fatal(err)
	}
	return integer
}

func flipBit(num int64) int64 {
	if num == 0 {
		return 1
	} else {
		return 0
	}
}

func filter(ss []string, place int, matchBit int64) (ret []string) {
	if len(ss) == 1 {
		return ss
	}
	for _, val := range ss {
		if (bitStrToInt(val)>>place)&1 == matchBit {
			ret = append(ret, val)
		}
	}
	return
}

func getBitCounts(input []string) []int64 {
	numDigits := len(input[0])
	bitCounts := make([]int64, numDigits)
	var place int
	for index := range input[0] {
		for _, value := range input {
			// Find out whether the number at the current binary
			// place is a 1 or a 0 and add it to the list
			place = numDigits - 1 - index
			bitCounts[index] += (bitStrToInt(value) >> place) & 1
		}
	}
	return bitCounts
}

func getMostCommonBits(input []string) []int64 {
	bitCounts := getBitCounts(input)

	bits := make([]int64, len(bitCounts))
	for index, val := range bitCounts {
		if float32(val) >= float32(len(input))/2.0 {
			bits[index] = 1
		} else {
			bits[index] = 0
		}
	}
	return bits
}

func day3Part2(input []string) int {
	// Find the oxygen generator rating
	oxygenGenerator := make([]string, len(input))
	mostCommonBits := make([]int64, len(input[0]))
	copy(oxygenGenerator, input)
	for len(oxygenGenerator) > 1 {
		for index := range input[0] {
			place := len(input[0]) - 1 - index
			mostCommonBits = getMostCommonBits(oxygenGenerator)
			oxygenGenerator = filter(oxygenGenerator, place, mostCommonBits[index])
		}
	}

	oxygenGeneratorRating := bitStrToInt(oxygenGenerator[0])

	// Find the co2 scrubber rating
	co2Scrubber := make([]string, len(input))
	copy(co2Scrubber, input)
	for len(co2Scrubber) > 1 {
		for index := range input[0] {
			place := len(input[0]) - 1 - index
			mostCommonBits = getMostCommonBits(co2Scrubber)
			co2Scrubber = filter(co2Scrubber, place, flipBit(mostCommonBits[index]))
		}
	}

	co2ScrubberRating := bitStrToInt(co2Scrubber[0])

	return int(oxygenGeneratorRating * co2ScrubberRating)
}
