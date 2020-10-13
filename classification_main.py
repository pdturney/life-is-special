#
# Classification Main
#
# Peter Turney, October 7, 2020
#
# Find a way to score the 2**18 possible outer-totalistic 
# automata rules, such that the Game of Life (and hopefully
# other universal cellular automata) gets a high score.
#
# https://www.conwaylife.com/wiki/List_of_Life-like_cellular_automata
#
import golly as g
import random as rand
import classification_functions as cfuncs
import classification_parameters as cparams
#
# name of file with a list of rules and CPUs
#
rule_file_name = cparams.rule_file_name
#
# density range for initial random matrix
#
density_range = cparams.density_range
#
# width and height for initial random square matrix
#
initial_size = cparams.initial_size
#
# number of steps for given run of simulation
#
num_steps = cparams.num_steps
#
# number of random trials to evaluate
#
num_trials = cparams.num_trials
#
# prepare log file for recording statistics
#
# - use option 0 so that log file writes immediately (no buffer), 
#   in case of forced exit (crash)
#
log_path = cparams.log_path
log_handle = open(log_path, "w", 0)
#
# find the CPU id for the current run
#
current_cpu_id = cparams.current_cpu_id
#
# read the rule list and extract rules that match the current
# run's CPU id
#
rule_list = cfuncs.tsv_BS_rule_cpu(rule_file_name, current_cpu_id)
#
# Golly screen magnification
#
screen_mag = cparams.screen_mag
#
# initialize Golly
#
g.setalgo("QuickLife") # select the algorithm for Golly
g.autoupdate(False) # do not update the view unless requested
g.new("Classification") # create an empty universe
g.setmag(screen_mag) # screen magnification
#
# show parameter settings in the log file
#
parameter_settings = cfuncs.show_parameters()
log_handle.write("\nParameter Settings\n\n")
for setting in parameter_settings:
  log_handle.write(setting + "\n")
log_handle.write("\n")
#
# write a header line for the list of results
#
columns = ["rule", \
           "prob pop incr", \
           "prob area incr", \
           "avg final area", \
           "avg final density"]
#
column_header = "\t".join(columns) + "\n"
#
log_handle.write(column_header)
#
# -------------------------------------------------
# main loop: iterate through the list of rules
# -------------------------------------------------
#
for rule in rule_list:
  #
  # initialize some variables
  #
  prob_pop_incr = 0.0 # probability of population increase
  prob_area_incr = 0.0 # probability of area increase
  avg_final_area = 0.0 # average final area
  avg_final_density = 0.0 # average final density
  prob_delta = 1.0 / num_trials # amount for updating probability
  #
  for trial in range(num_trials):
    #
    # show the rule and the trial number in the Golly header
    #
    g.show(rule + " -- trial " + str(trial + 1))
    #
    # initialize Golly
    #
    g.new("Classification") # make a new, empty Golly universe
    g.setmag(screen_mag) # screen magnification
    g.setrule(rule) # set the rule that Golly will use
    offset = int(initial_size / 2) # this centers the matrix in the display
    #
    # write initial matrix into the Golly universe
    #
    density = rand.uniform(density_range[0], density_range[1]) 
    for x in range(initial_size):
      for y in range(initial_size):
        if (rand.uniform(0, 1) <= density):
          g.setcell(x - offset, y - offset, 1) # set cell to 1
    #
    # initial population count
    #
    initial_pop_count = float(g.getpop())
    initial_bounding_box = g.getrect()
    initial_area = float(initial_size * initial_size)
    #
    # run Golly for num_steps
    #
    g.run(num_steps) 
    g.update() # update the Golly display
    #
    # final population count
    #
    final_pop_count = float(g.getpop())
    final_bounding_box = g.getrect()
    #
    # final area
    #
    if (len(final_bounding_box) == 0):
      final_area = 0.0
    else:
      [x, y, width, height] = final_bounding_box
      final_area = float(width * height)
    #
    # update probability of area increase
    #
    if (final_area > initial_area):
      prob_area_incr = prob_area_incr + prob_delta
    #
    # update probability of population increase
    #
    if (final_pop_count > initial_pop_count):
      prob_pop_incr = prob_pop_incr + prob_delta
    #
    # update density
    #
    if (final_area > 0.0):
      final_density = final_pop_count / final_area
    else:
      final_density = 0.0
    #
    # update average final area
    #
    area_delta = final_area / num_trials
    avg_final_area = avg_final_area + area_delta
    #
    # update average final density
    #
    density_delta = final_density / num_trials
    avg_final_density = avg_final_density + density_delta
    #
    # end of trial loop
    #
  #
  # report some statistics
  #
  row = [rule, prob_pop_incr, prob_area_incr, \
         avg_final_area, avg_final_density]
  format_row = "\t".join(map(str, row)) + "\n"
  log_handle.write(format_row)
  #
  # end of rule loop
  #
#
# close log file
#
log_handle.write("\nDone.\n")
log_handle.close()
# 
#