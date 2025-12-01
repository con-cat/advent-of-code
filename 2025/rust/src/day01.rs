use crate::helpers;

pub fn part_1() {
    if let Ok(lines) = helpers::read_lines("../input/day01.txt") {
        let mut zero_count = 0;
        let mut current_number = 50;

        for line in lines.map_while(Result::ok) {
            let (direction, num_clicks) = parse_line(line);

            current_number = rotate(current_number, direction, num_clicks);

            if current_number == 0 {
                zero_count += 1;
            }
        }

        println!("{}", zero_count)
    }
}

fn rotate(mut current_number: i32, direction: char, num_clicks: i32) -> i32 {
    let difference = num_clicks % 100;

    if direction == 'L' {
        current_number -= difference;
    } else if direction == 'R' {
        current_number += difference;
    } else {
        panic!("Unhandled direction");
    }

    if current_number < 0 {
        current_number += 100;
    } else if current_number > 99 {
        current_number -= 100;
    }

    current_number
}

fn parse_line(line: String) -> (char, i32) {
    let mut chars = line.chars();

    let direction: char = chars.next().expect("Can't parse direction");
    let num_clicks: i32 = chars
        .collect::<String>()
        .parse::<i32>()
        .expect("Can't parse num_clicks");

    (direction, num_clicks)
}
