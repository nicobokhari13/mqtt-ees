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
      4. See this for exception handling on system arguments too [Errors + Exceptions](https://docs.python.org/3/tutorial/errors.html)
2. Go through config files, determine standard indication for describing variables
3. Check for errors that may lead to `None` being evaluated for some crucial variable condition
4. Prepare `set_up` and `tear_down` functions or modules
   1. [Found reference on abstract class properties in python](https://www.geeksforgeeks.org/abstract-classes-in-python/)
5. Create run_experiment script to run an experiment of a specific type based on the user input
   1. For example, the `config_file = sys.argv[1]` could be used as a bash argument

-----BEGIN PGP PUBLIC KEY BLOCK-----

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
0mzHiPzUR7+KNWfO
=JYed
-----END PGP PUBLIC KEY BLOCK-----