import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import seaborn as sns
import statistics
import random
import csv

df = pd.read_csv("/content/savings_data_final.csv")

fig = px.scatter(df, y = "quant_saved", color = "rem_any")

fig.show()

with open('savings_data_final.csv', newline = "") as f:
  reader = csv.reader(f)
  savings_data = list(reader)

savings_data.pop(0)

total_entries = len(savings_data)

total_people_given_reminder = 0

for data in savings_data:
  if int(data[3]) == 1:
    total_people_given_reminder += 1

fig = go.Figure(go.Bar(x = ["Reminded", "Not Reminded"], y = [total_people_given_reminder, (total_entries - total_people_given_reminder)]))

fig.show()

all_savings = []

for data in savings_data:
  all_savings.append(float(data[0]))

print(f"Mean of savings - {statistics.mean(all_savings)}")

print(f"Median of savings - {statistics.median(all_savings)}")

print(f"Mode of savings - {statistics.mode(all_savings)}")

reminded_savings = []
not_reminded_savings = []
for data in savings_data:
  if int(data[3]) == 1:
    reminded_savings.append(float(data[0]))
  else:
    not_reminded_savings.append(float(data[0]))

print("Results for people who were reminded to save")

print(f"Mean of savings - {statistics.mean(reminded_savings)}")

print(f"Median of savings - {statistics.median(reminded_savings)}")

print(f"Mode of savings - {statistics.mode(reminded_savings)}")

print("\n\n")

print("Results for people who were not reminded to save")

print(f"Mean of savings - {statistics.mean(not_reminded_savings)}")

print(f"Median of savings - {statistics.median(not_reminded_savings)}")

print(f"Mode of savings - {statistics.mode(not_reminded_savings)}")

print(f"Standard deviation of all the data - {statistics.stdev(all_savings)}")

print(f"Standard deviation of people who were reminded - {statistics.stdev(reminded_savings)}")

print(f"Standard deviation of people who were not reminded - {statistics.stdev(not_reminded_savings)}")

age = []

savings = []

for data in savings_data:
  if float(data[5]) != 0:
    age.append(float(data[5]))
    savings.append(float(data[0]))

correlation = np.corrcoef(age, savings)
print(f"Correlation between the age of the person and their savings is - {correlation[0, 1]}")

fig = ff.create_distplot([df["quant_saved"].tolist()], ["Savings"], show_hist = False)

fig.show()

sns.boxplot(data = df, x = df["quant_saved"])

q1 = df["quant_saved"].quantile(0.25)

q3 = df["quant_saved"].quantile(0.75)
iqr = q3 - q1

print(f"Q1 - {q1}")

print(f"Q3 - {q3}")

print(f"IQR - {iqr}")

upper_whisker = q3 + 1.5 * iqr

lower_whisker = q1 - 1.5 * iqr

print(f"Lower Whisker - {lower_whisker}")

print(f"Upper Whisker - {upper_whisker}")

new_df = df[df["quant_saved"] < upper_whisker]

all_savings = new_df['quant_saved'].tolist()

print(f'Mean of Savings - {statistics.mean(all_savings)}')

print(f'Median of Savings - {statistics.median(all_savings)}')

print(f'Mode of Savings - {statistics.mode(all_savings)}')

print(f'Standard Deviation of Savings - {statistics.stdev(all_savings)}')

fig = ff.create_distplot([new_df['quant_saved'].tolist()], ['savings'], show_hist = False)

fig.show()

sampling_mean_list = []

for i in range(0, 1000):
  temp_list = []

  for j in range(100):
    temp_list.append(random.choice(all_savings))

    sampling_mean_list.append(statistics.mean(temp_list))

mean_sampling = statistics.mean(sampling_mean_list)

fig = ff.create_distplot([sampling_mean_list], ["Savings (Sampling)"], show_hist=False) 

fig.add_trace(go.Scatter(x=[mean_sampling, mean_sampling], y=[0, 0.1], mode="lines", name="MEAN")) 

fig.show()