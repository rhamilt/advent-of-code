require 'set'
def instantiate
	lines = File.open("7.txt").readlines.map(&:strip)
	prereqs = Hash.new { |prereqs, key| prereqs[key] =  []}
	postreqs = Hash.new { |postreqs, key| postreqs[key] =  []}
	actions = Set[]
	lines.each do |line|
		m = line.match /Step (.) must be finished before step (.) can begin./
		prereqs[m[1]] << m[2]
		postreqs[m[2]] << m[1]
		actions << m[1] << m[2]
	end
	q = []
	actions.each {|action| q << action if !postreqs.keys.include? action }; q.sort!
	return prereqs, postreqs, q
end

def p1
	prereqs, postreqs, q = instantiate
	result = ""
	while !q.empty?
		action = q.shift
		prereqs[action].each do |postreq|
			postreqs[postreq] -= [action]
			q << postreq if postreqs[postreq].empty?
		end
		result << action
		q.sort!
	end
	return result
end

def timeCalc(action)
	return 60 + "ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(action) + 1
end

def p2
	prereqs, postreqs, q = instantiate
	result = ""
	workers = {0 => "", 1 => "", 2 => "", 3 => "", 4 => ""}
	actions = {}
	time = -1
	while !q.empty? or workers.values.join != ""
		workers.keys.each do |worker|
			if actions[workers[worker]] == 1
				prereqs[workers[worker]].each do |postreq|
					postreqs[postreq] -= [workers[worker]]
					q << postreq if postreqs[postreq].empty?
				end
				q.sort!
				workers[worker] = ""
			else
				actions[workers[worker]] -= 1 if workers[worker] != ""
			end
			if workers[worker] == "" and !q.empty?
				workers[worker] = q.shift 
				actions[workers[worker]] = timeCalc(workers[worker])
			end
		end
		time += 1
	end
	return time
end

=begin part 1
	This actually came pretty quickly after I attempted it a second time (after about 10 days time)
	the double prereq/postreq dictionaries was very useful and useful as a double-edged tree type structure.
	I don't know if this method really counts as a toposort, but that's obviously what this was.
=end
puts p1

=begin part 2
	Man this also took me a lot longer than it should have. I figured out the structure pretty quickly but just
	couldn't get it right -- lots of bugs :(
=end
puts p2