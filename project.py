from datetime import date
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["average"].to_list()

mean = statistics.mean(data)
stdDev = statistics.stdev(data)

print("Mean of sample:- ", mean)
print("std_deviation of sample:- ", stdDev)
#fig = ff.create_distplot([data], ["temp"],show_hist=False)
# fig.show()

# code to find mean and std deviation of 100 data points
dataset = []

for i in range(0, 100):
    random_index = random.randint(0, len(data))
    value = data[random_index]
    dataset.append(value)

mean = statistics.mean(dataset)
std_deviation = statistics.stdev(dataset)
print("Mean of sample:- ", mean)
print("std_deviation of sample:- ", std_deviation)

# code to find the mean of 100 data points 1000 times and plot it
# function to get the mean of the given data samples
# pass the number of data points you want  as counter


def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[
                  0, 1], mode="lines", name="MEAN"))
    fig.show()


def standard_deviation():
    mean_list = []
    for i in range(0, 1000):
        setOfMeans = random_set_of_mean(100)
        mean_list.append(setOfMeans)

    standard_deviation = statistics.stdev(mean_list)
    print(standard_deviation)


standard_deviation()


def setup():
    mean_list = []
    for i in range(0, 1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)


setup()
