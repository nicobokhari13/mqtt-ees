# MQTT-EES

# TODO

1. Refactor main(copy of `main.py`) and export sensing capabilities, topics, subscribers, devices. etc to readable files? 
2. Consolidate all experiment similar functions/lines into one main file
3. Prepare `set_up` and `tear_down` functions or modules
4. Create run_experiment script to run an experiment of a specific type based on the user input
   1. For example, the `config_file = sys.argv[1]` could be used as a bash argument