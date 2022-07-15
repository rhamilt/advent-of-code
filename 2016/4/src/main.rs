use std::collections::HashMap;
use regex::Regex;

const ALPHA: &str = "abcdefghijklmnopqrstuvwxyz";

fn main() {
    let input = std::fs::read_to_string("../4.txt").unwrap();
    let re = Regex::new(r"(.*)(\d{3})\[(\w{5})\]").unwrap();
    let mut id_sum = 0;
    for line in input.lines() {
        // Parse the line into the code, id, and checksum
        let captures = re.captures_iter(line).next().unwrap();
        let code: String = captures.get(1).unwrap().as_str().to_string();
        let id: usize = captures.get(2).unwrap().as_str().parse().unwrap();
        let checksum: String = captures.get(3).unwrap().as_str().to_string();

        // Find frequencies of code
        let mut freqs: HashMap<char, u8> = HashMap::new();
        for ch in code.chars() {
            let count = freqs.entry(ch).or_insert(0);
            *count += 1;
        }
        freqs.remove(&'-');

        // Find top 5 characters by frequency (ties broken by alphabetization)
        let mut char_list: Vec<(char, u8)> = freqs.into_iter().collect();
        // Sort alphabetically
        char_list.sort();
        // Sort by frequency
        char_list.sort_by(|a, b| b.1.cmp(&a.1));
        let top_5: Vec<char> = char_list[..5].into_iter()
                                             .map(|a| a.0)
                                             .collect::<Vec<char>>();

        // Check that the checksum is correct
        if checksum == top_5.into_iter().collect::<String>() {
            id_sum += id;
        }

        let decoded_code = cypher(&code, id);
        if decoded_code.contains("north") {
            // part 2: Pretty straightforward, actually had the most trouble figuring out how to
            // store the alphabet for the purposes of the cypher. eventually settled on string
            // slice, but it was certainly annoying figuring out how to find the position of a
            // character in the alphabet. This whole thing was an issue because as of writing this
            // I have not actually learned about iterators
            println!("part 2: {}", id);
        }
    }

    // part 1: kind of a slog to get this, but I knew the strategy was to alphabetize and sort the
    // codes. Lots of work to learn regex, sort_by, and the equivalent of joining. 
    println!("part 1: {}", id_sum);
}

// Performs the caesar cypher on the code by shifting each character `id` times to the right
// Input : code: the string slice we are decoding
//         id  : the number of times we are shifting
// Return : The decoded string
fn cypher(code: &str, id: usize) -> String {
    let mut rotated: String = String::new();
    for ch in code.chars() {
        if ch == '-' { rotated.push(' '); continue; }
        let original_index = ALPHA.chars().position(|c| c == ch).unwrap();
        let new_index = (original_index + id) % ALPHA.len(); 
        rotated.push(ALPHA.chars().collect::<Vec<char>>()[new_index]); 
    }

    rotated
}
