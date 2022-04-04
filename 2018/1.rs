// Reed Hamilton
// rhamilt@uw.edu
// Copyright 2022 Reed Hamilton

use std::collections::HashSet;

fn main() {
  let changes = std::fs::read_to_string("1.txt").expect("it failed");
  let mut sum = 0;
  for change in changes.lines() { sum += change.parse::<i32>().unwrap(); }
  // Part 1: Easy, just getting used to the language
  println!("sum: {}", sum);

  let mut seen: HashSet<i32> = vec![].into_iter().collect();
  sum = 0;
  'outer: loop {
    for change in changes.lines() {
      sum += change.parse::<i32>().unwrap();
      if seen.contains(&sum) {
        // This feels like a very non-Rust solution, but it's in the name of
        // learning!
        println!("seen twice: {}", sum);
        break 'outer;
      }
      seen.insert(sum);
    }
  }
}
