use crate::helpers::read_file_to_string;
use std::collections::HashSet;

pub fn day_6(n: usize) -> usize {
    let input = read_file_to_string("../input/day06.txt");
    for (i, _c) in input.chars().enumerate() {
        let substring = &input[i..i + n];
        let set: HashSet<char> = substring.chars().collect();
        if substring.len() == set.len() {
            return i + n;
        }
    }
    return 0;
}
