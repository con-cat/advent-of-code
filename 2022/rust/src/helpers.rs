use std::fs;

pub fn read_file_to_string(path: &str) -> String {
    return fs::read_to_string(path).expect("Unable to read file");
}
