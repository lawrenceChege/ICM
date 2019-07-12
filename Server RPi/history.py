import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

df = pd.read_csv('histogram.csv', index_col = 'timestamp', parse_dates=True, infer_datetime_format=True)
graph = df[['x-axis', 'y-axis']].plot(title="Vibration Analysis")
graph.set_xlabel("Time")
graph.set_ylabel("Displacement - X")
plt.xticks(rotation=25)
plt.show()
