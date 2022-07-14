// Reed Hamilton
fn main() {
    let input: String = std::fs::read_to_string("../3.txt").unwrap();
    let mut count = 0;
    for line in input.lines() {
        let triangle = triangle(line);
        if check_validity(triangle) { count += 1; }
    }
    
    // part 1: very frustrated with the fact that there are varying number of spaces between the
    // triangle values. Eventually found the split_whitespace method but it just took a while
    println!("part 1: {}", count);

    let lines: Vec<&str> = input.lines().collect();
    count = 0;
    for i in (0..lines.len()).step_by(3) {
        let line1 = triangle(lines[i]); 
        let line2 = triangle(lines[i + 1]); 
        let line3 = triangle(lines[i + 2]); 
        if check_validity(vec![line1[0], line2[0], line3[0]]) { count += 1; }
        if check_validity(vec![line1[1], line2[1], line3[1]]) { count += 1; }
        if check_validity(vec![line1[2], line2[2], line3[2]]) { count += 1; }
    } 

    // part 2: straight forward, forgot to reset count so originally I was getting more valid
    // triangles than possible
    println!("part 2: {}", count)
}

// Converts 3 numbers in a string slice to a vector of i32's
fn triangle(line: &str) -> Vec<i32> {
    line.trim().split_whitespace().map(|s| s.parse().unwrap()).collect()
}

// Checks that the sum of two side lengths of a triangle is greater than the other side
fn check_validity(triangle: Vec<i32>) -> bool {
        triangle[0] + triangle[1] > triangle[2] &&
        triangle[0] + triangle[2] > triangle[1] &&
        triangle[1] + triangle[2] > triangle[0]
}
