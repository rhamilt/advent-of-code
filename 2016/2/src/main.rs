// Reed Hamilton

const GRID1: [[&str; 3]; 3] = [
    ["1", "2", "3"], 
    ["4", "5", "6"], 
    ["7", "8", "9"]
];
const GRID2: [[&str; 5]; 5] = [
    ["_", "_", "1", "_", "_"],
    ["_", "2", "3", "4", "_"],
    ["5", "6", "7", "8", "9"],
    ["_", "A", "B", "C", "_"],
    ["_", "_", "D", "_", "_"],
];

fn main() {
    let input = std::fs::read_to_string("../2.txt").unwrap();

    let mut coord1: (usize, usize) = (1, 1);
    let mut coord2: (usize, usize) = (2, 2);

    let mut code1: String = String::new();
    let mut code2: String = String::new();

    for line in input.lines() {
        for c in line.chars() {
            // part 1
            match c {
                'U' => if coord1.0 > 0 {coord1 = (coord1.0 - 1, coord1.1)},
                'D' => if coord1.0 < GRID1.len() {coord1 = (coord1.0 + 1, coord1.1)},
                'L' => if coord1.1 > 0 {coord1 = (coord1.0, coord1.1 - 1)},
                'R' => if coord1.1 < GRID1.len() {coord1 = (coord1.0, coord1.1 + 1)},
                _ => (),
            }

            // part 2
            match c {
                'U' => {
                    if coord2.0 > 0 && GRID2[coord2.0 - 1][coord2.1] != "_" {
                        coord2 = (coord2.0 - 1, coord2.1);
                    }
                }
                'D' => {
                    if coord2.0 < GRID2.len() && GRID2[coord2.0 + 1][coord2.1] != "_" {
                        coord2 = (coord2.0 + 1, coord2.1);
                    }
                }
                'L' => {
                    if coord2.1 > 0 && GRID2[coord2.0][coord2.1 - 1] != "_" {
                        coord2 = (coord2.0, coord2.1 - 1);
                    }
                }
                'R' => {
                    if coord2.1 < GRID2.len() && GRID2[coord2.0][coord2.1 + 1] != "_" {
                        coord2 = (coord2.0, coord2.1 + 1);
                    }
                }
                _ => (),
            }
        }

        code1.push_str(&GRID1[coord1.0 as usize][coord1.1 as usize]);
        code2.push_str(&GRID2[coord2.0][coord2.1]);
    }

    // part 1: pretty straight forward, I had a little trouble with integer overflow as index
    // requires usize, but my method of finding the max of 0 and possibly -1 requires integers
    // After going back and changing it, I found what I think is a better solution with an if, no
    // longer using std::cmp
    println!("part 1: {}", code1);
    // part 2: I don't think I did this a really bad way, just the if statements within the match
    // statement are kind of annoying to look at and hard to read.
    println!("part 2: {}", code2);
}
