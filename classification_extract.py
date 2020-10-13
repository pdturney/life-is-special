#
# Classification Extract
#
# Peter Turney, October 10, 2020
#
# Read in (1) a long list of sorted rules with various 
# statistics and (2) a short list of plain rules of
# interest.
#
# Write out (3) the subset of (1) that matches all of (2).
#
import golly as g
import classification_functions as cfuncs
import classification_parameters as cparams
#
# The files
#
# - (1) long list of sorted rules with various statistics
#
long_file_name = cparams.sorted_file_name
#
# - (2) short list of plain rules of interest
#
short_file_name = "turing-complete.txt"
#
# - (3) the subset of (1) that matches all of (2)
#
match_file_name = "turing-complete-extracted.txt"
#
# Read (1) the long file into a hash table indexed
# by the rule name.
#
long_file_handle = open(long_file_name, "r")
rule2line = {}
for line in long_file_handle:
  # line 1 =
  # "1	B3/S23	0.091	0.73	0.131866538031	4.0	0.242075787887"
  tuple = line.rstrip().split("\t")
  key = tuple[1] # B3/S23
  rule2line[key] = line
long_file_handle.close()
#
# Read (2) the short list of plain rules of interest.
#
short_file_handle = open(short_file_name, "r")
rule_list = []
for rule in short_file_handle:
  # "B3/S23"
  rule_list.append(rule.rstrip())
short_file_handle.close()
#
# Write (3) the subset of (1) that matches all of (2).
#
match_file_handle = open(match_file_name, "w")
for key in rule_list:
  line = rule2line[key]
  match_file_handle.write(line)
match_file_handle.close()
#
#