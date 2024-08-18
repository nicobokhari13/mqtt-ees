# Walkthrough of `main.py`

## Outside of main function

- acquire config file from system input
- perform config file setup
- set up file paths for experiment results (publisher, subscriber, topic, and threshold)
- create containers for publishers, subscriber, and topic
- set other attributes + constants
- instantiate global instance of system capability

`setup_exp_vary_pub`, `setup_exp_vary_sub`, `setup_exp_vary_topic`
- randomize variable between 3 & max defined by configuration file
- subscription frequencies defined with 
  - default or experiment # of subscribers
  - number of subscriptions randomized between 1 - num topics
  - subscriptions is a random sample of topics from topic container
  - subscription freq = range from min to max freq
  - topic frequency is updated via topic container helper function `updateQoS`
  - every topic ensured subscription via subscriber container helper function `ensureTopicCoverage`
- devices are set up with publisher container helper function `generateDeviceCapability`
- topic container sets up expected timestamps
- system capability is created for each topic based on the device's 
- NO THRESHOLD VARIANCE FUNCTIONS
  - uses `setup_default` to set defaults, threshold is manually varied with config file
`experiment_setup` function
- difference in setup between varying pub,sub,topic,and "default"
- create sense timestamps 
