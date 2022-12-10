use crate::helpers::read_file_to_string;

fn parse_line(line: &str) -> (&str, i32) {
    let split: Vec<&str> = line.split(" ").collect();
    if split.len() > 1 {
        return (split[0], split[1].parse::<i32>().unwrap());
    } else {
        return (split[0], -1);
    }
}

// PART 1

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

pub fn part_1() -> i32 {
    let input = read_file_to_string("../input/day10.txt");
    let mut cpu = CPU {
        x: 1,
        cycle_count: 0,
    };
    let mut interesting_results: i32 = 0;
    for line in input.lines() {
        let (command, number) = parse_line(line);
        let result: Option<i32>;
        if command == "noop" {
            result = cpu.noop();
        } else if command == "addx" {
            result = cpu.addx(number);
        } else {
            panic!("Can't parse input");
        }
        if result != None {
            interesting_results += result.unwrap();
        }
    }
    return interesting_results;
}

// PART 2

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
            if self.get_position() == 0 {
                self.next_row();
            }
        }
    }
    fn next_row(&mut self) {
        self.rows.push(self.current_row.to_string());
        self.current_row = "".to_string()
    }
    fn add_pixel(&mut self) {
        let pixel = self.get_pixel();
        self.current_row.push_str(pixel);
    }
    fn get_pixel(&self) -> &'static str {
        let position = self.get_position();
        let x_range = (self.x - 1)..(self.x + 2);
        if self.get_sprite_range().contains(&position) {
            return "#";
        } else {
            return ".";
        }
    }
    fn get_position(&self) -> i32 {
        return self.cycle_count % 40;
    }
    fn get_sprite_range(&self) -> std::ops::Range<i32> {
        return (self.x - 1)..(self.x + 2);
    }
}

pub fn part_2() {
    let input = read_file_to_string("../input/day10.txt");
    let mut crt = CRT {
        x: 1,
        cycle_count: 0,
        rows: Vec::new(),
        current_row: "".to_string(),
    };
    for line in input.lines() {
        let (command, number) = parse_line(line);
        if command == "noop" {
            crt.noop();
        } else if command == "addx" {
            crt.addx(number);
        } else {
            panic!("Can't parse input");
        }
    }
    for row in crt.rows {
        println!("{:?}", row);
    }
}
