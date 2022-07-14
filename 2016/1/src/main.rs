use std::fs;
use std::collections::HashSet;

// A lot of this was probably better done with tuples, but I haven't thought
// about tuples in a while since I've mostly been using C/C++ and Java
const DIRS: [[i32; 2]; 4] = [[0, 1], [1, 0], [0, -1], [-1, 0]];

fn main() {
    let instructions = fs::read_to_string("../1.txt")
        .expect("Couldn't read");

    let mut coord: [i32; 2] = [0, 0];
    let mut seen: HashSet<[i32; 2]> = HashSet::new();
    let mut path_crossed: bool = false;
    let mut dir: usize = 0;

    for instruc in instructions.split(", ") {
        let val: i32 = (&instruc[1..]).parse().unwrap();
        dir = if instruc.starts_with("L") {(dir + 3) % 4} else {(dir + 1) % 4};
        for _ in 0..val {
            coord[0] += DIRS[dir][0];
            coord[1] += DIRS[dir][1];
            if seen.contains(&coord) && !path_crossed {
                // Part 2: I thought I would have a lot more issues with storing
                // arrays in a HashSet, but it worked how I expected and this
                // went swimmingly
                println!("part 2: {}", manhattan_distance(&coord));
                path_crossed = true;
            }
            seen.insert([coord[0], coord[1]]);
        }
    }

    // Part 1: Pretty straightforward no issues in completing this other than
    // syntax lookups
    println!("part 1: {}", manhattan_distance(&coord));
}

fn manhattan_distance(coord: &[i32; 2]) -> i32 {
    coord[0].abs() + coord[1].abs()
}