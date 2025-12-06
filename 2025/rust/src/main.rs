#![allow(unused)]
mod day01;
mod day02;
mod day03;
mod day04;
mod day05;
mod helpers;

fn main() {
    let input_path = "../input/day05.txt";
    let result = day05::part_2(input_path);
    println!("{}", result);
}
