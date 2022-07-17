use fancy_regex::Regex;

fn main() {
    let input = std::fs::read_to_string("../7.txt").unwrap();

    // Regex patterns for ips that have contain letters with the pattern "abba", but not in bracket
    // aaaa is not included
    let abba_match = Regex::new(r"(\w)(?!\1)(\w)\2\1").unwrap();
    let abba_match_bracket = Regex::new(r"\[\w*(\w)(?!\1)(\w)\2\1\w*\]").unwrap();
    
    // patterns for ips that contain letters with pattern "aba" and "bab" in brackets
    // "aaa" is not included
    let aba_bab_match = Regex::new(r"(\w)(?!\1)(\w)\1.*\[\w*\2\1\2\w*\]").unwrap();
    let aba_bab_match_reverse = Regex::new(r"\[\w*(\w)(?!\1)(\w)\1\w*\].*\2\1\2").unwrap();

    let mut count1 = 0;
    let mut count2 = 0;
    for ip in input.lines() {
        // Check if it matches for part 1
        if abba_match.is_match(ip).unwrap() {
            if !abba_match_bracket.is_match(ip).unwrap() {
                count1 += 1;
            }
        }

        // check if it matches for part 2
        if aba_bab_match.is_match(ip).unwrap() {
            if bracket_match(&aba_bab_match, ip){
                count2 += 1;
            }
        } else if aba_bab_match_reverse.is_match(ip).unwrap() {
            if bracket_match(&aba_bab_match_reverse, ip){
                count2 += 1;
            }
        }
    }

    // part 1: 2 problems: 1) regular regex does not support back references 2) I was using .
    // instead of \w so the captures for the second one was spanning in between brackets to capture
    // things that should not have been captured
    println!("part 1: {}", count1);
    // part 2: this is incorrect (off by 1) and I cannot figure out why. Probably a case I am
    // missing. Had to remember to check that one of the matches is actually outside the brackets.
    // This is why there is a second if in the if statements for part2
    println!("part 2: {}", count2);
}

// Checks if there is an equivalent number of left and right brackets in a given regex match
fn bracket_match(pattern: &Regex, ip: &str) -> bool {
    let match_content = pattern.captures(ip).unwrap().unwrap();
    let match_text = match_content.get(0).unwrap().as_str();
    match_text.matches('[').count() == match_text.matches(']').count()
}
