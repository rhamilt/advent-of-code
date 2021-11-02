require 'set'

data = File.open('1.txt').readlines.map(&:strip).map(&:to_i)
p data.sum

curr = 0
seen = Set[]
data.cycle do |datum|
	curr += datum
	(puts curr; break) if seen.include? curr
	seen << curr
end