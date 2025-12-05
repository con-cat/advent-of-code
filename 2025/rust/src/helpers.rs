use std::fs;
use std::io;
use std::io::BufRead;
use std::path::Path;

pub fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<fs::File>>>
where
    P: AsRef<Path>,
{
    let file = fs::File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

pub fn read_file_to_string(file_path: &str) -> Result<String, io::Error> {
    let content = fs::read_to_string(file_path)?;

    Ok(content)
}

pub fn string_to_number_range(string: &str) -> std::ops::RangeInclusive<isize> {
    // Turn a string like "11-22" into an inclusive range of numbers
    let numbers: Vec<_> = string.split("-").collect();
    let start = numbers[0].parse::<isize>().expect("Cannot parse start");
    let end = numbers[1].parse::<isize>().expect("Cannot parse end");

    start..=end
}
