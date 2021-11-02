lines = File.open("7.txt").read.split("\n")#.map(&:to_i)
rules = Hash.new { |hash, key| hash[key] = [] }
contains = Hash.new { |hash, key| hash[key] = [] }
lines.each do |line|
	bags = line.split(/bags?/)
	bags.map! {|x| x.strip}.select! {|x| x.size > 1}
	bags[1..bags.size].each do |bag|
		count, color = bag.match(/(\d*)? (\w+ \w+)$/).captures
		rules[color] << bags[0]
		contains[bags[0]] << [count.to_i, color] if color != "no other"
	end
end

def count(frontier, rules, contains, p2=false)
	seen = []
	total = 0
	while frontier.size != 0
		temp = frontier.pop
		bagCount, bag = !p2 ? [0, temp]: temp
		if p2 || !seen.include?(bag)
			temp = !p2 ? rules[bag]: contains[bag]
			total += bagCount
			temp.each do |x|
				frontier << (!p2 ? x: [x[0] * bagCount, x[1]])
			end
			seen << bag
		end
	end
	return !p2 ? seen.size: total
end
p count(rules["shiny gold"].clone, rules, contains)
p count(contains["shiny gold"].clone, rules, contains, true)