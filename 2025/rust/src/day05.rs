use crate::helpers;

pub fn part_1(input_path: &str) -> isize {
    let mut fresh_ingredient_count = 0;
    let (ranges, ingredient_ids) = parse_input_file(input_path);

    for ingredient_id in ingredient_ids {
        for range in &ranges {
            if range.contains(&ingredient_id) {
                fresh_ingredient_count += 1;
                break;
            }
        }
    }

    fresh_ingredient_count
}

fn parse_input_file(input_path: &str) -> (Vec<std::ops::RangeInclusive<isize>>, Vec<isize>) {
    let mut ranges = Vec::new();
    let mut ingredient_ids = Vec::new();

    if let Ok(lines) = helpers::read_lines(input_path) {
        let mut blank_line_seen = false;

        for line in lines.map_while(Result::ok) {
            if line == "" {
                blank_line_seen = true;
                continue;
            }
            if !blank_line_seen {
                ranges.push(helpers::string_to_number_range(&line));
            } else {
                ingredient_ids.push(line.parse::<isize>().expect("Cannot parse ingredient id"));
            }
        }
    }

    (ranges, ingredient_ids)
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT_PATH: &str = "../input/test_day05.txt";

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(INPUT_PATH), 3);
    }
}
