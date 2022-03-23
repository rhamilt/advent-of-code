class Packet
	def initialize(trans)
		@trans = trans
		@version = trans[0...3].to_i(2)
		@tag = trans[3...6].to_i(2)
		@subPackets = []
		idx = 6
		if @tag == 4
			literal = ""
			#Pretty "rubynic"
			literal << trans[idx+1...idx+=5] while trans[idx] != "0"
			literal << trans[idx+1...idx+=5]
			@trans = @trans[0...idx] #Just so trans is correct to size
			@literalVal = literal.to_i(2)
		else
			@lengthTypeID = trans[idx].to_i
			idx += 1
			if @lengthTypeID == 0
				#I just discoverd you can use += in an expression like this as if it's ++
				#Pretty amazing
				totalBitslength = trans[idx...idx+=15].to_i(2)
				subByBitLength(trans[idx...], totalBitslength)
			else
				packetsContained = trans[idx...idx+=11].to_i(2)
				subByNumPackets(trans[idx..], packetsContained)
			end
		end
		#Making sure our packet is actually the right size, really only useful for debug
		@trans = @trans[..packetLength]
	end

	#I know these two methods do two very similar things, but it seems like a 
	#pain to combine them
	def subByBitLength (trans, bitLength)
		idx = 0
		while idx < bitLength
			@subPackets << Packet.new(trans[idx..])
			idx += @subPackets[-1].packetLength
		end
		@trans = @trans[..packetLength]
	end

	def subByNumPackets (trans, packetsContained)
		numPacks = 0
		idx = 0
		while numPacks < packetsContained
			@subPackets << Packet.new(trans[idx..])
			numPacks += 1
			idx += @subPackets[-1].packetLength
		end
		@trans = @trans[..packetLength]
	end

	def packetLength
		if @tag == 4
			return @trans.length
		elsif @lengthTypeID == 0
			return 22 + @subPackets.map { |sP| sP.packetLength }.sum
		else
			return 18 + @subPackets.map { |sP| sP.packetLength }.sum
		end
	end

	def versionSum #Part 1
		return @version + @subPackets.map{ |sP| sP.versionSum }.sum
	end

	def evaluate #Part 2
		case @tag # Don't even have to add returns to all of these!
		when 0
			@subPackets.map {|sP| sP.evaluate}.sum
		when 1
			@subPackets.map {|sP| sP.evaluate}.inject(:*)
		when 2
			@subPackets.map {|sP| sP.evaluate}.min
		when 3
			@subPackets.map {|sP| sP.evaluate}.max
		when 4
			return @literalVal
		when 5
			(@subPackets[0].evaluate > @subPackets[1].evaluate) ? 1 : 0
		when 6
			(@subPackets[0].evaluate < @subPackets[1].evaluate) ? 1 : 0
		when 7
			(@subPackets[0].evaluate == @subPackets[1].evaluate) ? 1 : 0
		end
	end
end
