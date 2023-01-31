#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from:)([A-Z]+)?([a-z]+)?(\+?[0-9]+)?/).join
puts ARGV[0].scan(/(?<=to:)([A-Z]+)?([a-z]+)?(\+?[0-9]+)?/).join
puts ARGV[0].scan(/(?<=flags:)([0-9\-:]+)?/).join
