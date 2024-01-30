#!/usr/bin/env ruby

regex = /School/
string = ARGV[0]

match = string.match(regex)
puts match.to_s
