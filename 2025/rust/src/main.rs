#![allow(unused)]
mod day01;
mod day02;
mod day03;
mod helpers;

fn main() {
    let input_path = "../input/day03.txt";
    let result = day03::part_2(input_path);
    println!("{}", result);
}
