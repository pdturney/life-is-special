#
# Classification Initialize
#
# Peter Turney, October 8, 2020
#
# The goal here is to spread the job of analysis of each of
# the rules over several CPUs. The output of this routine
# will be a text file in which each line has the following form:
#
# <rule such as "B3/S23"> <tab> <CPU such as "CPU2">
#
import golly as g
import random as rand
import classification_functions as cfuncs
import classification_parameters as cparams
#
# make a list of B/S rules (born/survive -- outer-totalistic)
#
rules_list = cfuncs.all_BS_rules()
#
# open a file for storing selected rules
#
rule_file_name = cparams.rule_file_name
rule_file_handle = open(rule_file_name, "w")
#
# write the rules to the file
#
for rule in rules_list:
  # randomly assign a cpu to this rule
  cpu_num = rand.randint(1, cparams.num_cpus)
  rule_and_cpu = rule + "\tCPU" + str(cpu_num)
  # write the rule to the file
  rule_file_handle.write(rule_and_cpu + "\n")
#
# close file
#
rule_file_handle.close()
#