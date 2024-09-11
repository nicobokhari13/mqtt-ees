# MQTT-EES

Start in the root project directory. 
The following experiment modes are available: `energy`,`lifespan`

The following schedulers are supported: `ees`, `random`, `mqtt`

For more help with using the simulation flags run: `python3 start.py --help`

## Example: 2 Experiments 
Energy Consumption Demo 

```bash
python3 start.py -config config/example_energy.ini -mode energy -scheds ees,random
```

Lifespan Demo
```bash
python3 start.py -config config/example_lifespan.ini -mode lifespan -scheds ees,random,mqtt
```


