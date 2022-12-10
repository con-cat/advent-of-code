use std::collections::HashSet;
use std::fs;

fn read_file_to_string(path: &str) -> String {
    return fs::read_to_string(path).expect("Unable to read file");
}

// fn day_6(n: usize) -> usize {
//     let input = read_file_to_string("../input/day06.txt");
//     for (i, _c) in input.chars().enumerate() {
//         let substring = &input[i..i + n];
//         let set: HashSet<char> = substring.chars().collect();
//         if substring.len() == set.len() {
//             return i + n;
//         }
//     }
//     return 0;
// }

struct CPU {
    x: i32,
    cycle_count: i32,
}

impl CPU {
    pub fn noop(&mut self) -> Option<i32> {
        return self.add_to_cycle_count(1);
    }
    pub fn addx(&mut self, n: i32) -> Option<i32> {
        let strength = self.add_to_cycle_count(2);
        self.x += n;
        return strength;
    }
    fn add_to_cycle_count(&mut self, n: i32) -> Option<i32> {
        let mut interesting_strength = None;
        for _i in 0..n {
            self.cycle_count += 1;
            if (self.cycle_count - 20) % 40 == 0 {
                interesting_strength = Some(self.cycle_count * self.x);
            }
        }
        return interesting_strength;
    }
}

struct CRT {
    rows: Vec<String>,
    current_row: String,
    x: i32,
    cycle_count: i32,
}

impl CRT {
    pub fn noop(&mut self) {
        self.add_to_cycle_count(1);
    }
    pub fn addx(&mut self, n: i32) {
        self.add_to_cycle_count(2);
        self.x += n;
    }
    fn add_to_cycle_count(&mut self, n: i32) {
        for _i in 0..n {
            self.add_pixel();
            self.cycle_count += 1;
            if self.cycle_count % 40 == 0 {
                self.clear_current_row();
            }
        }
    }
    fn clear_current_row(&mut self) {
        self.rows.push(self.current_row.to_string());
        self.current_row = "".to_string()
    }
    fn add_pixel(&mut self) {
        let pixel = self.get_pixel();
        self.current_row.push_str(pixel);
    }
    fn get_pixel(&mut self) -> &'static str {
        let position = self.cycle_count % 40;
        let x_range = (self.x - 1)..(self.x + 2);
        if x_range.contains(&position) {
            return "#";
        } else {
            return ".";
        }
    }
}

fn day_10_part_1() -> i32 {
    let input = read_file_to_string("../input/day10.txt");
    let mut cpu = CPU {
        x: 1,
        cycle_count: 0,
    };
    let mut interesting_results: i32 = 0;
    for line in input.lines() {
        let split: Vec<&str> = line.split(" ").collect();
        let result: Option<i32>;
        if split[0] == "noop" {
            result = cpu.noop();
        } else if split[0] == "addx" {
            result = cpu.addx(split[1].parse::<i32>().unwrap());
        } else {
            panic!("Can't parse input");
        }
        if result != None {
            interesting_results += result.unwrap();
        }
    }
    return interesting_results;
}

fn day_10_part_2() {
    let input = read_file_to_string("../input/day10.txt");
    let mut crt = CRT {
        x: 1,
        cycle_count: 0,
        rows: [].to_vec(),
        current_row: "".to_string(),
    };
    for line in input.lines() {
        let split: Vec<&str> = line.split(" ").collect();
        if split[0] == "noop" {
            crt.noop();
        } else if split[0] == "addx" {
            crt.addx(split[1].parse::<i32>().unwrap());
        } else {
            panic!("Can't parse input");
        }
    }
    for row in crt.rows {
        println!("{:?}", row);
    }
}

fn main() {
    println!("Part 1: {:?}\n", day_10_part_1());
    day_10_part_2();
}
