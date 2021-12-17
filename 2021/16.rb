#Refer to Packet.rb for most of the good stuff on Packets
load "Packet.rb"

transHex = File.open("16.txt").read.strip
trans = transHex.to_i(16).to_s(2)

packet = Packet.new(trans)

=begin part 1
	What a doozy. Didn't do it day of, but tried to do it on the plane with a lot of frustration.
	Ended up scrapping my code for the "subBy" functions and it became a lot simpler. Would estimate
	I spent about 2.5 hours on this, mostly debugging why the semi-recursive packet parsing wasn't
	working.
=end
p packet.versionSum

=begin part 2
	Very easy when I used an object like this. Just evaluate the root node and everything else will
	follow. Pretty clean case statements above. About 5 extra minutes after p1.
=end
p packet.evaluate