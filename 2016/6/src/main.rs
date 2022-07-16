use std::collections::HashMap;

fn main() {
    let input = std::fs::read_to_string("../6.txt").unwrap();
    
    // Create frequencies maps for each position of the messages (8 total)
    let mut position_frequencies: Vec<HashMap<char, i32>> = Vec::new();
    for _ in 0..8 {
        position_frequencies.push(HashMap::<char, i32>::new());
    }

    for message in input.lines() {
        // Update the frequencies in each position for a given message
        let mut i = 0;
        for ch in message.chars() { 
            let count = position_frequencies[i].entry(ch).or_insert(0); 
            *count += 1;
            i += 1;
        }
    }

    // Convert from vector of hashmaps to vector of vectors
    let mut frequency_lists: Vec<Vec<(char, i32)>> = Vec::new();
    for frequencies in position_frequencies {
       frequency_lists.push(frequencies.into_iter().collect::<Vec<(char, i32)>>()); 
    }

    // Sort each list by frequency (reverse for part 2) and append the most/least common to our
    // result strings
    let mut result_most_common: String = String::new(); 
    let mut result_least_common: String = String::new(); 
    for mut char_position_frequencies in frequency_lists {
        char_position_frequencies.sort_by(|a, b| b.1.cmp(&a.1)); 
        result_most_common.push(char_position_frequencies[0].0);
        char_position_frequencies.sort_by(|a, b| a.1.cmp(&b.1)); 
        result_least_common.push(char_position_frequencies[0].0);
    }

    // part 1: The way to do this was pretty straightforward, just surprised at what stuff worked
    // out with having a vector of HashMaps (I am still confused on how the inner HashMaps are
    // mutable)
    println!("part 1: {}", result_most_common);
    // part 2: very easy, just needed to add a couple (mostly copied) lines to just reverse sort
    // the frequencies
    println!("part 2: {}", result_least_common);
}
