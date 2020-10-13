#
# Classification Sort
#
# Peter Turney, October 10, 2020
#
# Read in all of the score files, merge them, and
# then sort them.
#
import golly as g
import classification_functions as cfuncs
import classification_parameters as cparams
#
# make a list of the score file names
#
log_prefix = cparams.log_prefix
num_cpus = cparams.num_cpus
#
log_file_list = []
#
for cpu_num in range(num_cpus):
  log_file_name = log_prefix + str(cpu_num + 1) + ".txt"
  log_file_list.append(log_file_name)
#
# read the score files into a list
#
score_list = []
#
for log_file in log_file_list:
  log_handle = open(log_file, "r")
  for line in log_handle:
    # if the line starts with "B" then ...
    if (line[0] == "B"):
      #
      # input line format:
      #
      #   0 rule              -- B3/S23
      #   1 prob pop incr     -- 0.094
      #   2 prob area incr    -- 0.778
      #   3 avg final area    -- 516.715
      #   4 avg final density -- 0.136
      #
      # split line string into a list (tuple)
      #
      tuple = line.rstrip().split("\t")
      #
      # break out the parts of the tuple
      #
      rule = tuple[0]
      prob_pop_incr = float(tuple[1])
      prob_area_incr = float(tuple[2])
      avg_final_area = float(tuple[3])
      avg_final_density = float(tuple[4])
      #
      # calculate the summary score
      #
      gm_prob_pop_incr = cfuncs.geo_mean(prob_pop_incr)
      gm_prob_area_incr = cfuncs.geo_mean(prob_area_incr)
      rule_complexity = cfuncs.complexity(rule)
      #
      score = 0.0 # default score
      #
      if ((gm_prob_pop_incr > 0.0) and \
          (gm_prob_area_incr > 0.0) and \
          (avg_final_density > 0.0) and \
          (rule_complexity > 0.0)):
        # higher numerator is better
        numerator = gm_prob_pop_incr * gm_prob_area_incr
        # lower denominator  is better
        denominator = avg_final_density * rule_complexity
        # calculate the score
        score = numerator / denominator 
      #
      # output line format:
      #
      #   0 rule              -- B3/S23
      #   1 prob pop incr     -- 0.094
      #   2 prob area incr    -- 0.778
      #   3 avg final density -- 0.136
      #   4 rule complexity   -- 4
      #   5 score             -- 0.242
      #
      new_tuple = [rule, \
                   prob_pop_incr, \
                   prob_area_incr, \
                   avg_final_density, \
                   rule_complexity, \
                   score]
      #
      # append new_tuple to score_list
      #
      score_list.append(new_tuple)
      #
    #
  # close the file
  log_handle.close()
#
# sort the list in order of decreasing scores and
# sequentially number the items in the list
#
sorted_tuples = sorted(score_list, key=lambda x: x[5], \
                       reverse=True)
#
# write the list to a file
#
sorted_file_name = cparams.sorted_file_name
sorted_handle = open(sorted_file_name, "w", 0)
#
item_num = 1
#
for tuple in sorted_tuples:
  # add item_num to the beginning of the tuple
  new_tuple = [item_num] + tuple
  # convert items in tuple to strings, then join them with tabs
  line = "\t".join(map(str, new_tuple)) + "\n"
  # write line to file
  sorted_handle.write(line)
  # update item_num
  item_num = item_num + 1
#
sorted_handle.close()
#
#
#