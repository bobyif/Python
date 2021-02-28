from capture import df
from bokeh.plotting import figure, show, output_file

p = figure(x_axis_type="datetime", height=500, width=1000, title="Motion graph")
p.yaxis.minor_tick_line_color = None
p.yaxis[0].ticker.desired_num_ticks = 1

q = p.quad(left=df["Start"], right=df["End"], top=1, bottom=0, color="blue")
output_file("Time_detected2.html")
show(p)
