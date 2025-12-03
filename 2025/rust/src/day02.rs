pub fn part_1(input: &str) -> i64 {
    let mut total = 0;
    let lines: Vec<_> = input.split(",").collect();
    for line in lines {
        let num_range = parse_line(&line);

        for number in num_range {
            if !is_valid_id(number) {
                total += number;
            }
        }
    }

    total
}

pub fn part_2(input: &str) -> i64 {
    let mut total = 0;
    let lines: Vec<_> = input.split(",").collect();
    for line in lines {
        let num_range = parse_line(line);

        for number in num_range {
            if has_repeated_substring_pattern(&number.to_string()) {
                total += number;
            }
        }
    }

    total
}

fn parse_line(line: &str) -> std::ops::RangeInclusive<i64> {
    let numbers: Vec<_> = line.split("-").collect();
    let start = numbers[0].parse::<i64>().expect("Cannot parse start");
    let end = numbers[1].parse::<i64>().expect("Cannot parse end");

    start..=end
}

fn is_valid_id(number: i64) -> bool {
    let number_str = number.to_string();
    let length = number_str.len();

    if length == 1 {
        true
    } else {
        let first_part = &number_str[0..length / 2];
        let second_part = &number_str[length / 2..length];

        first_part != second_part
    }
}

fn has_repeated_substring_pattern(s: &str) -> bool {
    // https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
    let n = s.len();
    let mut prefix = vec![0; n];
    let bytes = s.as_bytes();
    let mut j = 0;

    // Build the prefix table
    for i in 1..n {
        while j > 0 && bytes[i] != bytes[j] {
            j = prefix[j - 1];
        }
        if bytes[i] == bytes[j] {
            j += 1;
        }
        prefix[i] = j;
    }

    // Check for repetition
    let last_value = prefix[n - 1];
    last_value > 0 && n % (n - last_value) == 0
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT: &str = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124";

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(INPUT), 1227775554);
    }

    #[test]
    fn test_part_2() {
        assert_eq!(part_2(INPUT), 4174379265);
    }

    #[test]
    fn test_parse_line() {
        let line = "11-22";

        assert_eq!(parse_line(line), 11..=22)
    }

    #[test]
    fn test_is_valid_id() {
        assert_eq!(is_valid_id(55), false);
        assert_eq!(is_valid_id(6464), false);
        assert_eq!(is_valid_id(123123), false);
        assert_eq!(is_valid_id(101), true);
    }

    #[test]
    fn test_has_repeated_substring_pattern() {
        assert_eq!(has_repeated_substring_pattern("12341234"), true);
        assert_eq!(has_repeated_substring_pattern("123123123"), true);
        assert_eq!(has_repeated_substring_pattern("1212121212"), true);
        assert_eq!(has_repeated_substring_pattern("1111111"), true);
        assert_eq!(has_repeated_substring_pattern("12345"), false);
    }
}
