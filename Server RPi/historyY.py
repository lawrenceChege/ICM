import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

df = pd.read_csv('histogram.csv', index_col = 'timestamp', parse_dates=True, infer_datetime_format=True)
graph = df[['y-axis']].plot(title="Vibration Analysis")
graph.set_xlabel("Time")
graph.set_ylabel("Displacement - Y")
plt.xticks(rotation=25)
graphx = df[['x-axis']].plot(title="Vibration Analysis")
graphx.set_xlabel("Time")
graphx.set_ylabel("Displacement - x")
plt.xticks(rotation=25)
plt.show()
