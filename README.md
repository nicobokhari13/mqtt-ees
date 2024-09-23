# MQTT-EES

Start in the root project directory. 
The following experiment modes are available: `energy`,`lifespan`

The following schedulers are supported: `ees`, `random`, `mqtt`

For more help with using the simulation flags run: `python3 start.py --help`

## Example: 2 Experiments 
Energy Consumption Demo 

```sh
python3 start.py -config config/example_energy_pub.ini -mode energy -scheds ees,random
```

Lifespan Demo

```sh
python3 start.py -config config/example_lifespan.ini -mode lifespan -scheds ees,random,mqtt
```

## Reading Results Column Headers

The following headers are standard across all results csv files:

`algo_name, time_end, num_round, num_topic, num_pubs, num_subs, total_energy_consumption`


`time_end` - if a single device's battery reduces to 0 as the tasks generated for the observation period are allocated, then the simulated algorithm ends execution and logs the associated shutdown time 

`num_round` - the simulated round number

`total_energy_consumption` - the total amount of energy the system of devices used to perform all sensing tasks within the observation period

Additional values appended to each row are the energy consumptions of `num_pubs` devices at the end of round `num_round`

## Example: Reading Results
For example: 
`ees,NA,2,8,3,8,1.0035000000000007,0.3405000000000002,0.32750000000000024,0.33550000000000024`
- algo_name: ees
- time_end: NA (the system did not shut down)
- num_round = 2
- num_topic = 8
- num_pubs = 3
- num_subs = 8
- total_energy_consumption = 1.0035000000000007
The system tracked 3 devices' consumptions: 
`0.3405000000000002,0.32750000000000024,0.33550000000000024`
(You can double check that the sum is equivalent to the value in the `total_energy_consumption` column)

