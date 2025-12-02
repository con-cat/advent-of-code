pub fn part_1(input: String) -> i64 {
    let mut total = 0;
    let lines: Vec<_> = input.split(",").collect();
    for line in lines {
        let num_range = parse_line(line.to_string());

        for number in num_range {
            if !is_valid_id(number) {
                total += number;
            }
        }
    }

    total
}

fn parse_line(line: String) -> std::ops::RangeInclusive<i64> {
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

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        let input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124";
        assert_eq!(part_1(input.to_string()), 1227775554);
    }

    #[test]
    fn test_parse_line() {
        let line = "11-22".to_string();

        assert_eq!(parse_line(line), 11..=22)
    }

    #[test]
    fn test_is_valid_id() {
        assert_eq!(is_valid_id(55), false);
        assert_eq!(is_valid_id(6464), false);
        assert_eq!(is_valid_id(123123), false);
        assert_eq!(is_valid_id(101), true);
    }
}
