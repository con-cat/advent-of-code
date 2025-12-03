use crate::helpers;

pub fn part_1(input_path: &str) -> u32 {
    let mut total_joltage = 0;
    if let Ok(lines) = helpers::read_lines(input_path) {
        for line in lines.map_while(Result::ok) {
            total_joltage += get_joltage(&line)
        }
    }
    total_joltage
}

fn get_joltage(line: &str) -> u32 {
    // Turn the string into a vector of numbers
    let numbers: Vec<u32> = line.chars().filter_map(|c| c.to_digit(10)).collect();
    let numbers_len = numbers.len();
    let max_number = numbers
        .iter()
        .cloned()
        .max()
        .expect("numbers contains no items");

    // Get the index of the maximum number
    let max_index = numbers
        .iter()
        .position(|&x| x == max_number)
        .expect("The maximum number will have an index");

    // Find the digits of the joltage
    let tens: u32;
    let ones: u32;
    let remaining_numbers: &[u32];
    if max_index == numbers_len - 1 {
        // The maximum number is the last one in the vector
        remaining_numbers = &numbers[..max_index];
        tens = remaining_numbers
            .iter()
            .cloned()
            .max()
            .expect("remaining_numbers contains no items");
        ones = max_number;
    } else {
        remaining_numbers = &numbers[max_index + 1..];
        tens = max_number;
        ones = remaining_numbers
            .iter()
            .cloned()
            .max()
            .expect("remaining_numbers contains no items")
    }

    tens * 10 + ones
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT_PATH: &str = "../input/test_day03.txt";

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(INPUT_PATH), 357);
    }

    #[test]
    fn test_get_joltage() {
        assert_eq!(get_joltage("987654321111111"), 98);
        assert_eq!(get_joltage("811111111111119"), 89);
        assert_eq!(get_joltage("234234234234278"), 78);
        assert_eq!(get_joltage("818181911112111"), 92);
    }
}
