use std::collections::HashSet;
use std::fs;

fn read_file_to_string(path: &str) -> String {
    return fs::read_to_string(path).expect("Unable to read file");
}

fn day_6(n: usize) -> usize {
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

fn main() {
    println!("Part 1: {:?}", day_6(4));
    println!("Part 2: {:?}", day_6(14));
}
