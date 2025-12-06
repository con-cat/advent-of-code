use crate::helpers;
use std::cmp::max;
use std::cmp::min;

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

pub fn part_2(input_path: &str) -> isize {
    let (mut ranges, _) = parse_input_file(input_path);

    // Sort ranges by start then end
    ranges.sort_by(|a, b| {
        // First compare the start values
        let start_cmp = a.start().cmp(&b.start());
        if start_cmp == std::cmp::Ordering::Equal {
            // If start values are equal, compare the end values
            a.end().cmp(&b.end())
        } else {
            start_cmp
        }
    });

    // Find the unions of all the ranges.
    let mut overlapping_ranges: Vec<std::ops::RangeInclusive<isize>> = Vec::new();
    let mut current_range = ranges[0].clone();
    for range in ranges {
        if range.start() > current_range.end() {
            // The ranges don't intersect at all.
            overlapping_ranges.push(current_range.clone());
            current_range = range;
            continue;
        }
        // Calculate the union of range and current_range
        let start = min(current_range.start(), range.start());
        let end = max(current_range.end(), range.end());
        current_range = *start..=*end;
    }
    overlapping_ranges.push(current_range.clone());

    // Count the ingredient ids in overlapping_ranges
    let mut fresh_ingredient_count = 0;
    for range in overlapping_ranges {
        fresh_ingredient_count += range.end() + 1 - range.start();
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

    #[test]
    fn test_part_2() {
        assert_eq!(part_2(INPUT_PATH), 14);
    }
}
