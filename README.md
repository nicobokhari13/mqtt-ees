# MQTT-EES

Start in the root project directory. 
The following experiment modes are available: `energy`,`lifespan`

The following schedulers are supported: `ees`, `random`, `mqtt`

## Example: 2 Experiments 
Energy Consumption Demo 

```bash
python3 start.py -config config/example_energy.ini -mode energy -scheds ees,random
```

Lifespan Demo
```bash
python3 start.py -config config/example_lifespan.ini -mode lifespan -scheds ees,random,mqtt
```


