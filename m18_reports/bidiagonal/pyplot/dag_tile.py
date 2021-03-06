#!/home/mawussi/anaconda2/bin/python
from graphviz import Digraph
import seaborn as sns
dot = Digraph(comment="Panel Oriented DAG")
dot.graph_attr['rankdir'] = 'TB'
dot.attr("node", style="filled", color=sns.xkcd_rgb["red"])
dot.attr("edge", splines="curved")
dot.node("qr_1", "GEQRT(1,1)")
# TSQRT kernels on the first panel
dot.attr("node", style="filled", color=sns.xkcd_rgb["light red"])
dot.node("tsqrt_2", "TSQRT(2,1)")
dot.node("tsqrt_3", "TSQRT(3,1)")
dot.node("tsqrt_4", "TSQRT(4,1)")
dot.node("tsqrt_5", "TSQRT(5,1)")
# Upate first tile-row zunmqr
dot.attr("node", style="filled", color=sns.xkcd_rgb["green"])
dot.node("zunmqr_2","ZUNMQR(1,2)")
dot.node("zunmqr_3","ZUNMQR(1,3)")
dot.node("zunmqr_4","ZUNMQR(1,4)")
dot.node("zunmqr_5","ZUNMQR(1,5)")
dot.attr("node", style="filled", color=sns.xkcd_rgb["faded green"])
# Update  second tile-row with TSMQR  kernels
dot.node("tsmqr_22","TSMQR(2,2)")
dot.node("tsmqr_23","TSMQR(2,3)")
dot.node("tsmqr_24","TSMQR(2,4)")
dot.node("tsmqr_25","TSMQR(2,5)")
# Update  third tile-row with TSMQR  kernels
dot.node("tsmqr_32","TSMQR(3,2)")
dot.node("tsmqr_33","TSMQR(3,3)")
dot.node("tsmqr_34","TSMQR(3,4)")
dot.node("tsmqr_35","TSMQR(3,5)")
# Update  fourth tile-row with TSMQR  kernels
dot.node("tsmqr_42","TSMQR(4,2)")
dot.node("tsmqr_43","TSMQR(4,3)")
dot.node("tsmqr_44","TSMQR(4,4)")
dot.node("tsmqr_45","TSMQR(4,5)")
# Update  fifth tile-row with TSMQR  kernels
dot.node("tsmqr_52","TSMQR(5,2)")
dot.node("tsmqr_53","TSMQR(5,3)")
dot.node("tsmqr_54","TSMQR(5,4)")
dot.node("tsmqr_55","TSMQR(5,5)")


#Add edges for the first tile-row
dot.edge("qr_1",    "zunmqr_2")
dot.edge("qr_1",    "zunmqr_3")
dot.edge("qr_1",    "zunmqr_4")
dot.edge("qr_1",    "zunmqr_5")
#Add edges from zunmqr to first tsqrt
dot.edge("zunmqr_2", "tsqrt_2")
dot.edge("zunmqr_3", "tsqrt_2")
dot.edge("zunmqr_4", "tsqrt_2")
dot.edge("zunmqr_5", "tsqrt_2")
# Add edges for the update 2nd tile-row

#Add edges second tsqrt
dot.edge("tsqrt_2",    "tsqrt_3")
#Add edges third tsqrt
dot.edge("tsqrt_3",    "tsqrt_4")
#Add edges fourth tsqrt
dot.edge("tsqrt_4",    "tsqrt_5")

dot.edge("tsqrt_2", "tsmqr_22")
dot.edge("tsqrt_2", "tsmqr_23")
dot.edge("tsqrt_2", "tsmqr_24")
dot.edge("tsqrt_2", "tsmqr_25")

#Add edges for update third panel
dot.edge("tsqrt_3", "tsmqr_32")
dot.edge("tsqrt_3", "tsmqr_33")
dot.edge("tsqrt_3", "tsmqr_34")
dot.edge("tsqrt_3", "tsmqr_35")


#Add edges for update fourth panel
dot.edge("tsqrt_4", "tsmqr_42")
dot.edge("tsqrt_4", "tsmqr_43")
dot.edge("tsqrt_4", "tsmqr_44")
dot.edge("tsqrt_4", "tsmqr_45")

#Add edges for update fourth panel
dot.edge("tsqrt_5", "tsmqr_52")
dot.edge("tsqrt_5", "tsmqr_53")
dot.edge("tsqrt_5", "tsmqr_54")
dot.edge("tsqrt_5", "tsmqr_55")

#Save the file
dot.render("../fig/dag_tile")
dot.view()
