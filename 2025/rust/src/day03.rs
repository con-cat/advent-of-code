use crate::helpers;

pub fn part_1(input_path: &str) -> u64 {
    let mut total_joltage = 0;
    if let Ok(lines) = helpers::read_lines(input_path) {
        for line in lines.map_while(Result::ok) {
            total_joltage += get_joltage(&line, 2)
        }
    }
    total_joltage
}

pub fn part_2(input_path: &str) -> u64 {
    let mut total_joltage = 0;
    if let Ok(lines) = helpers::read_lines(input_path) {
        for line in lines.map_while(Result::ok) {
            total_joltage += get_joltage(&line, 12)
        }
    }
    total_joltage
}

fn get_joltage(line: &str, target_digits: usize) -> u64 {
    // Remove K digits to get the largest possible integer

    // Turn the string into a vector of numbers
    let numbers: Vec<u32> = line.chars().filter_map(|c| c.to_digit(10)).collect();

    // Find the number of digits to remove
    let mut k = numbers.len() - target_digits;

    let mut stack: Vec<u32> = Vec::new();

    for number in numbers {
        while k > 0
            && !stack.is_empty()
            && stack.last().expect("There are items in the stack") < &number
        {
            stack.pop();
            k -= 1;
        }
        stack.push(number);
    }

    digits_to_integer(&stack[..target_digits])
}

fn digits_to_integer(digits: &[u32]) -> u64 {
    let mut result = 0;
    let mut multiplier = 1;

    for &digit in digits.iter().rev() {
        result += digit as u64 * multiplier;
        multiplier *= 10;
    }

    result
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
        assert_eq!(get_joltage("987654321111111", 2), 98);
        assert_eq!(get_joltage("811111111111119", 2), 89);
        assert_eq!(get_joltage("234234234234278", 2), 78);
        assert_eq!(get_joltage("818181911112111", 2), 92);
        assert_eq!(get_joltage("987654321111111", 12), 987654321111);
        assert_eq!(get_joltage("811111111111119", 12), 811111111119);
        assert_eq!(get_joltage("234234234234278", 12), 434234234278);
        assert_eq!(get_joltage("818181911112111", 12), 888911112111);
    }

    #[test]
    fn test_digits_to_integer() {
        assert_eq!(digits_to_integer(&[1, 3, 4]), 134);
    }
}
