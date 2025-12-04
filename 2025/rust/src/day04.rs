use crate::helpers;

const DIRECTIONS: [(isize, isize); 8] = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
];

const ROLL: char = '@';

pub fn part_1(input_path: &str) -> usize {
    let roll_map = parse_input_file(input_path);
    let rows: isize = roll_map.len().try_into().unwrap();
    let columns: isize = roll_map[0].len().try_into().unwrap();

    // Check how many neighbouring rolls each roll in the map has.
    let mut accessible_rolls = 0;

    for i in 0..rows {
        for j in 0..columns {
            if roll_map[i as usize][j as usize] != ROLL {
                continue;
            }
            // Count each roll's neighbouring rolls
            let mut neighbour_roll_count = 0;
            for (di, dj) in DIRECTIONS {
                let target_i = i as isize + di;
                let target_j = j as isize + dj;
                if target_i >= 0 && target_i < rows && target_j >= 0 && target_j < columns {
                    if roll_map[target_i as usize][target_j as usize] == ROLL {
                        neighbour_roll_count += 1;
                    }
                }
            }
            if neighbour_roll_count < 4 {
                accessible_rolls += 1;
            }
        }
    }

    accessible_rolls
}

pub fn part_2(input_path: &str) -> usize {
    let mut roll_map = parse_input_file(input_path);
    let rows: isize = roll_map.len().try_into().unwrap();
    let columns: isize = roll_map[0].len().try_into().unwrap();

    let mut has_accessible_rolls = true;
    let mut rolls_removed_count = 0;

    while has_accessible_rolls {
        let mut accessible_roll_count = 0;
        for i in 0..rows {
            for j in 0..columns {
                if roll_map[i as usize][j as usize] != ROLL {
                    continue;
                }
                // Count each roll's neighbouring rolls
                let mut neighbour_roll_count = 0;
                for (di, dj) in DIRECTIONS {
                    let target_i = i + di;
                    let target_j = j + dj;
                    if target_i >= 0 && target_i < rows && target_j >= 0 && target_j < columns {
                        if roll_map[target_i as usize][target_j as usize] == ROLL {
                            neighbour_roll_count += 1;
                        }
                    }
                }
                if neighbour_roll_count < 4 {
                    accessible_roll_count += 1;
                    rolls_removed_count += 1;
                    roll_map[i as usize][j as usize] = '.';
                }
            }
        }
        if accessible_roll_count == 0 {
            has_accessible_rolls = false;
        }
    }

    rolls_removed_count
}

fn parse_input_file(input_path: &str) -> Vec<Vec<char>> {
    let mut rows = Vec::new();
    if let Ok(lines) = helpers::read_lines(input_path) {
        for line in lines.map_while(Result::ok) {
            rows.push(line.chars().collect())
        }
    }

    rows
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT_PATH: &str = "../input/test_day04.txt";

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(INPUT_PATH), 13);
    }

    #[test]
    fn test_part_2() {
        assert_eq!(part_2(INPUT_PATH), 43);
    }
}
