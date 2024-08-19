# MQTT-EES

# TODO : Add the following to jira

1. Read `config-*.ini` in `config` folder
   1. Reorganize [this](/mqtt-ees/config/config-ees-lifespan.ini) config to the template
   2. Determine template config
   3. Remove default_num_* variable from pubs, subs, and topic. use default boolean method variable
   4. Create ConfigFileMonitor
2. Go through config files, determine standard indication for describing variables
3. Check for errors that may lead to `None` being evaluated for some crucial variable condition
4. Prepare `set_up` and `tear_down` functions or modules
5. Create run_experiment script to run an experiment of a specific type based on the user input
   1. For example, the `config_file = sys.argv[1]` could be used as a bash argument