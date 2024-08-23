# MQTT-EES

1. Read `config-*.ini` in `config` folder
   1. Reorganize [this](/mqtt-ees/config/config-ees-lifespan.ini) config to the template
   2. Determine template config
   3. Identify where configuration is overloaded into publisher methods
   4. See if `None` type is supported in ConfigParser
      1. [Found reference](https://docs.python.org/3/library/configparser.html)
      2. Replace with configuration and set_default = false
      3. Use default_num_* = -1 for config -> experiment verification 
   5. Remove default_num_* variable from pubs, subs, and topic. use default boolean method variable (see bookmarks)
   6. Remove energies from pubs, 
   7. Create ConfigFileMonitor 
      1. See [**`config-example.ini`**](/config/config-example.ini)
      2. See [**`config_monitor.py`**](/config/config_monitor.py)
      3. [Found exception handling for config validation](https://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python)
2. Go through config files, determine standard indication for describing variables
3. Check for errors that may lead to `None` being evaluated for some crucial variable condition
4. Prepare `set_up` and `tear_down` functions or modules
   1. [Found reference on abstract class properties in python](https://www.geeksforgeeks.org/abstract-classes-in-python/)
5. Create run_experiment script to run an experiment of a specific type based on the user input
   1. For example, the `config_file = sys.argv[1]` could be used as a bash argument