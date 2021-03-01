from capture import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

p = figure(x_axis_type="datetime", height=500, width=1000, title="Motion graph")
p.yaxis.minor_tick_line_color = None
p.yaxis[0].ticker.desired_num_ticks = 1

hover = HoverTool(tooltips=[("Start:", "@Start_string"), ("End", "@End_string")])
p.add_tools(hover)

q = p.quad(left="Start", right="End", top=1, bottom=0, color="blue", source=cds)
output_file("Time_detected2.html")
show(p)
