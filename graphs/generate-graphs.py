import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

avg_energy_consumption_v_num_topics = "Average Energy Consumption (%) vs Number of Topics"
avg_energy_consumption_v_num_pubs = "Average Energy Consumption (%) vs Number of Publishers"
avg_energy_consumption_v_num_subs = "Average Energy Consumption (%) vs Number of Subscribers"
avg_energy_consumption_v_tailwindow = "Average Energy Consumption (%) vs Tail Window (ms)"
avg_energy_reduction_w_all_vars = "Average Energy Reduction (%) across all 4 experiments"
avg_lifespan_vs_algs = "Average System Lifespan (Hours) v Algorithms"
line_width = "2.0"
ees_line_color = 'g'
random_line_color = 'r'
mqtt_line_color = 'b'


raw_data_file = "/home/owner/repos/research/data/mqttees-graph-data.xlsx"
pub_sheet = "pub-line-graph"
sub_sheet = "sub-line-graph"
topic_sheet = "topic-line-graph"
tailwindow_sheet = "tailwindow-bar-graph"
lifespan_sheet = "lifespan-bar-graph"


all_raw_data = pd.read_excel(
    raw_data_file, 
    sheet_name=[
        pub_sheet, 
        sub_sheet, 
        topic_sheet,
        tailwindow_sheet,
        lifespan_sheet
    ]
) 

# Data Frames for each sheet
tailwindow_df = all_raw_data[tailwindow_sheet]
publisher_df = all_raw_data[pub_sheet]
subscriber_df = all_raw_data[sub_sheet]
topic_df = all_raw_data[topic_sheet]
lifespan_df = all_raw_data[lifespan_sheet]

# print(tailwindow_df)
# print(publisher_df)
# print(subscriber_df)
# print(topic_df)
# print(lifespan_df)

## create x axis for line graphs
num_pubs = publisher_df['# Publishers']
num_subs = subscriber_df['# Subscribers']
num_topics = topic_df["# Topics"]
size_tailwindow = ["100", "250", "500", "1000"]
algs = ["EES", "Random",  "MQTT"]
x_tailwindow = np.arange(len(size_tailwindow))
x_algs = np.arange(len(algs))
## create y axis for line graphs

# EES Consumptions Y values
ees_consumption_pub = publisher_df['EES']
ees_consumption_sub = subscriber_df['EES']
ees_consumption_topic = topic_df['EES']
ees_consumption_tailwindow = tailwindow_df['EES']

# Random Consumption Y values
random_consumption_pub = publisher_df['Random']
random_consumption_sub = subscriber_df['Random']
random_consumption_topic = topic_df['Random']
random_consumption_tailwindow = tailwindow_df['Random']
print('before set reduction')
# Reductions Distributions (for boxplot)
reduction_pub = publisher_df['Reduction']
reduction_sub = subscriber_df['Reduction']
reduction_topic = topic_df['Reduction']
reduction_tailwindow = tailwindow_df['Reduction']
# Life span values
random_avg_lifespan = lifespan_df['Random']
ees_avg_lifespan = lifespan_df['EES']
mqtt_avg_lifespan = lifespan_df['MQTT']
lifespans = [random_avg_lifespan, ees_avg_lifespan, mqtt_avg_lifespan]

# Create Publisher Line Graph
plt.figure(avg_energy_consumption_v_num_pubs)
#plt.title(avg_energy_consumption_v_num_pubs)
plt.plot(num_pubs, ees_consumption_pub, color = ees_line_color, lw = line_width, label="EES")
plt.plot(num_pubs, random_consumption_pub, color = random_line_color, lw = line_width, label="Random")
plt.xlabel("Number of Publishers")
plt.ylabel("Average Energy Consumption (%)")
plt.grid()
plt.legend()
plt.savefig(avg_energy_consumption_v_num_pubs)


# Create Subscriber Line Graph
plt.figure(avg_energy_consumption_v_num_subs)
#plt.title(avg_energy_consumption_v_num_subs)
plt.plot(num_subs, ees_consumption_sub, color = ees_line_color, lw = line_width, label = "EES")
plt.plot(num_subs, random_consumption_sub, color = random_line_color, lw = line_width, label="Random")
plt.xlabel("Number of Subscribers")
plt.ylabel("Average Energy Consumption (%)")
plt.grid()
plt.legend()
plt.savefig(avg_energy_consumption_v_num_subs)

# Create Topic Line Graph
plt.figure(avg_energy_consumption_v_num_topics)
#plt.title(avg_energy_consumption_v_num_topics)
plt.plot(num_topics, ees_consumption_topic, color = ees_line_color, lw = line_width, label = "EES")
plt.plot(num_topics, random_consumption_topic, color = random_line_color, lw = line_width, label = "Random")
plt.xlabel("Number of Topics")
plt.ylabel("Average Energy Consumption (%)")
plt.grid()
plt.legend()
plt.savefig(avg_energy_consumption_v_num_topics)

# Create Tail Window Bar Graph
plt.figure(avg_energy_consumption_v_tailwindow)
#plt.title(avg_energy_consumption_v_tailwindow)
plt.bar(x=x_tailwindow-0.2, height=ees_consumption_tailwindow,width=0.4 , label="EES", color=ees_line_color)
plt.bar(x=x_tailwindow+0.2, height=random_consumption_tailwindow, width=0.4, label="Random", color=random_line_color)
plt.xlabel("Tail Window (ms)")
plt.xticks(x_tailwindow, size_tailwindow)
plt.ylabel("Average Energy Consumption (%)")
plt.grid()
plt.legend()
plt.savefig(avg_energy_consumption_v_tailwindow)

# Create System Lifespan Bar Graph

plt.figure(avg_lifespan_vs_algs)
#plt.title(avg_lifespan_vs_algs)
plt.bar(x="EES", height=ees_avg_lifespan,width=0.5 , label="EES", color=ees_line_color)
plt.text(x="EES", y=float(ees_avg_lifespan.iloc[0]), s="{:.2f}".format(ees_avg_lifespan.iloc[0]))

plt.bar(x="Random", height=random_avg_lifespan, width=0.5, label="Random", color=random_line_color)
plt.text(x="Random", y=float(random_avg_lifespan.iloc[0]), s="{:.2f}".format(random_avg_lifespan.iloc[0]))

plt.bar(x="MQTT", height=mqtt_avg_lifespan, width = 0.5, label="MQTT", color=mqtt_line_color)
plt.text(x="MQTT", y=float(mqtt_avg_lifespan.iloc[0]), s="{:.2f}".format(mqtt_avg_lifespan.iloc[0]))

plt.xlabel("Algorithm")
plt.xticks(x_algs, algs)
plt.ylabel("Average System Lifespan (Hours)")
plt.legend()
plt.savefig(avg_lifespan_vs_algs)


# Create Reductions Box plot

distributions = {"# Publishers":reduction_pub, " # Subscribers":reduction_sub, "# Topics":reduction_topic, "Tail Window (ms)":reduction_tailwindow}

plt.figure(avg_energy_reduction_w_all_vars)
plt.boxplot(distributions.values(), tick_labels=distributions.keys(), showfliers=False)
plt.grid()
plt.ylabel("Energy Reduction (%)")
#plt.title(avg_energy_reduction_w_all_vars)
plt.savefig(avg_energy_reduction_w_all_vars)
# print(num_pubs)
# print(num_subs)
# print(num_topics)
# print(size_tailwindow)
# x_axis = file['X values'] 
# y_axis = file['Y values'] 
# plt.bar(x_axis, y_axis, width=5) 
# plt.xlabel("X-Axis") 
# plt.ylabel("Y-Axis") 
# plt.show() 
