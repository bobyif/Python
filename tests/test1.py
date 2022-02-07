# import functions
import pandas as pd
from bokeh.plotting import figure, show

# importing data from excel
data = pd.read_excel(r"C:\Users\mason\Desktop\Excel Python Testing.xlsx")
df_index_date = pd.DataFrame(data, columns=["A2:A116"])
df_index_us = pd.DataFrame(data, columns=["E2:E116"])
df_index_jp = pd.DataFrame(data, columns=["D2:D116"])

df_index_date = df_index_date.to_json()
df_index_us = df_index_us.to_json()
df_index_jp = df_index_jp.to_json()
print(df_index_jp, df_index_us, df_index_date)

# Defining data
x = [df_index_date]
y1 = [df_index_us]
y2 = [df_index_jp]

# axis titles
title = "Stock Market Returns: US vs. Japan"
x_axis_label = "Date"
y_axis_label = "Returns"

# create new plot with title and axis labels
p = figure(title=title, x_axis_label=x_axis_label, y_axis_label=y_axis_label)

# graphing line
p.line(x, y1, legend_label="U.S.", color="blue", line_width=2)
p.line(x, y2, legend_label="Japan", color="red", line_width=2)

# show results
show(p)