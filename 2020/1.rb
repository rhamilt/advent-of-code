lines = File.open('1.txt').readlines.map(&:strip).map(&:to_i)
lines.each do |first|
	lines.each do |second|
		if first + second  == 2020
			puts first * second 
		end
		lines.each do |third|
			if first + second + third == 2020
				puts first * second * third
			end
		end
	end
end

#Who cares if it's brute force ... it didn't take very long to write
#better solution in python:
#lines = list(map(int, open('1.txt', r).readlines()))
#for i in range(len(lines)):
#    for j in range(i + 1, len(lines)):
#        print (lines[i] * lines[j]) if lines[i] + lines[j] == 2020
#        for k in range(j + 1, len(lines)):
#            print (lines[i] * lines[j] * lines[k]) if lines[i] + lines[j] + lines[k]== 2020