#!/usr/bin/env ruby
A = ARGV[0].scan(/(?<=from:)(.\d+)/)
B = ARGV[0].scan(/(?<=to:)(.\d+)/)
C = ARGV[0].scan(/(?<=flags:)([0-9|:|-]+)/)
Lists = [A, B, C]
puts Lists.join(',')
