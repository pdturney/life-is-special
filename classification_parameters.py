#
# Classification Parmeters
#
# Peter Turney, October 10, 2020
#
# Set various parameters for running experiments
#
#
#
# name of file containing B/S rules
#
rule_file_name = "all-semitotalistic-rules.txt"
#
# density range for initial random matrix
#
density_range = [0.0, 1.0]
#
# width and height for initial random square matrix
# of boolean values
#
initial_size = 16
#
# number of steps for given run of simulation
#
num_steps = 50
#
# number of trials to evaluate for each rule
#
num_trials = 1000
#
# screen magnification for Golly
#
screen_mag = 2 # mag 3 = ratio 1:8
#
# number of CPUs to use 
#
num_cpus = 6
#
# the ID number of the CPU to use for the current run
# - ranges from 1 to num_cpus
#
current_cpu_id = 6
#
# path to log file for recording statistics
#
log_prefix = "all-semitotalistic-scores-CPU"
#
log_path = log_prefix + str(current_cpu_id) + ".txt"
#
# parameters for calculating rule complexity
#
complexity_BZ = 0 # for rules of the form "B0..."
complexity_BN = -2 # for rules of the form "BN..." N > 0
#
# file for merged and sorted statistics
#
sorted_file_name = "all-semitotalistic-sorted-rules.txt"
#
#