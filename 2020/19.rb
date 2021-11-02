require "Set"
def worksForZero(rule, rules)
	seen, frontier = Set.new(["0"]), [["0"]]
	while frontier.size > 0
		strList = frontier.pop
		str = strList.join(" ")
		strList.each do |char|
			if !"ab".include? char
				rules[char].size.times do |i|
					replaced = str.sub(/(^| )#{char}( |$)/, '\1' + rules[char][i] + '\2')
					return true if replaced.split.join == rule
					if rule.start_with? replaced.split(/\d/)[0].strip.split.join
						if !seen.include? replaced
							frontier << replaced.split
							seen << replaced
						end
					end
				end
				break
			end
		end
	end
	return false
end

valid, received = File.open("19.txt").read.split("\n\n")
rules = {}
valid.split("\n").each do |rule|
	num, possibles = rule.split(": ")
	rules[num] = possibles.split(" | ").map {|x| x.gsub(/"/, "")}
end

p received.split("\n").select {|message| worksForZero(message, rules)}.size
rules["8"] = ["4", "42 8"]
rules["11"] = ["42 31", "42 11 31"]
p received.split("\n").select {|message| worksForZero(message, rules)}.size