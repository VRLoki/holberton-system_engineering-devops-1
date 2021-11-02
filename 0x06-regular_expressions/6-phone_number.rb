#!/usr/bin/env ruby
#!/usr/bin/env ruby
# Ruby script that accepts one argument and
# pass it to a regularexpression matching method
puts ARGV[0].scan(/^\d{10,10}$/).join