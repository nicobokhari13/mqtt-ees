# MQTT-EES

## Current Stream 
1. Investigate config types and possible values
   1. See if `None` type is supported in ConfigParser
   2. [Found reference](https://docs.python.org/3/library/configparser.html)
   3. Replace with configuration and set_default = false
   4. Use default_num_* = -1 for config -> experiment verification 
   5. Remove default_num_* variable from pubs, subs, and topic. use default boolean method variable (see bookmarks)
   6. Remove energies from pubs, 
2. 
3. Once config data is determined, investigate bash script writing + necessary vs. optional flags
4. Create run_experiment script to run an experiment of a specific type based on the user input
   1. For example, the `config_file = sys.argv[1]` could be used as a bash argument

## Priority List

- Prepare `set_up` and `tear_down` functions or modules
  - [Found reference on abstract class properties in python](https://www.geeksforgeeks.org/abstract-classes-in-python/)
- Check for errors that may lead to `None` being evaluated for some crucial variable condition

## Completed 

- Read `config-*.ini` in `config` folder
- Reorganize [this](/mqtt-ees/config/config-ees-lifespan.ini) config to the template
- Determine template config
- Identify where configuration is overloaded into publisher methods

   4. Create ConfigFileMonitor 
      1. See [**`config-example.ini`**](/config/config-example.ini)
      2. See [**`config_monitor.py`**](/config/config_monitor.py)
      3. [Found exception handling for config validation](https://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python)
      4. See this for exception handling on system arguments too [Errors + Exceptions](https://docs.python.org/3/tutorial/errors.html)



