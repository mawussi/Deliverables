#!/home/mawussi/anaconda2/bin/python
from graphviz import Digraph
import seaborn as sns
dot = Digraph(comment="Panel Oriented DAG")
dot.attr("node", style="filled", color=sns.xkcd_rgb["red"])
#dot.attr("edge", splines="curved")
dot.node("qr_1", "GEQRT(0,0)")
# TSQRT kernels on the first panel
dot.attr("node", style="filled", color=sns.xkcd_rgb["light red"])
dot.node("tsqrt_2", "TSQRT(1,0)")
dot.node("tsqrt_3", "TSQRT(2,0)")
dot.node("tsqrt_4", "TSQRT(3,0)")
dot.node("tsqrt_5", "TSQRT(4,0)")
# Upate first tile-row zunmqr
dot.attr("node", style="filled", color=sns.xkcd_rgb["green"])
dot.node("zunmqr_2","ZUNMQR(0,1)")
dot.node("zunmqr_3","ZUNMQR(0,2)")
dot.node("zunmqr_4","ZUNMQR(0,3)")
dot.node("zunmqr_5","ZUNMQR(0,4)")
dot.attr("node", style="filled", color=sns.xkcd_rgb["faded green"])
# Update  second tile-row with TSMQR  kernels
dot.node("tsmqr_22","TSMQR(1,1)")
dot.node("tsmqr_23","TSMQR(1,2)")
dot.node("tsmqr_24","TSMQR(1,3)")
dot.node("tsmqr_25","TSMQR(1,4)")
# Update  third tile-row with TSMQR  kernels
dot.node("tsmqr_32","TSMQR(2,1)")
dot.node("tsmqr_33","TSMQR(2,2)")
dot.node("tsmqr_34","TSMQR(2,3)")
dot.node("tsmqr_35","TSMQR(2,4)")
# Update  fourth tile-row with TSMQR  kernels
dot.node("tsmqr_42","TSMQR(3,1)")
dot.node("tsmqr_43","TSMQR(3,2)")
dot.node("tsmqr_44","TSMQR(3,3)")
dot.node("tsmqr_45","TSMQR(3,4)")
# Update  fifth tile-row with TSMQR  kernels
dot.node("tsmqr_52","TSMQR(4,1)")
dot.node("tsmqr_53","TSMQR(4,2)")
dot.node("tsmqr_54","TSMQR(4,3)")
dot.node("tsmqr_55","TSMQR(4,4)")
#dot.node("lq_1", "GELQT(0,1)")

#Add edges for the first panel factorization
dot.edge("qr_1", "tsqrt_2")
dot.edge("tsqrt_2", "tsqrt_3")
dot.edge("tsqrt_3", "tsqrt_4")
dot.edge("tsqrt_4", "tsqrt_5")
# Add edges for the update of the first tile-row
dot.edge("qr_1", "zunmqr_2")
dot.edge("qr_1", "zunmqr_3")
dot.edge("qr_1", "zunmqr_4")
dot.edge("qr_1", "zunmqr_5")
#Add edges for the second tile-row update
dot.edge("zunmqr_2", "tsmqr_22")
dot.edge("tsqrt_2", "tsmqr_22")
dot.edge("zunmqr_3", "tsmqr_23")
dot.edge("tsqrt_2", "tsmqr_23")
dot.edge("zunmqr_4", "tsmqr_24")
dot.edge("tsqrt_2", "tsmqr_24")
dot.edge("zunmqr_5", "tsmqr_25")
dot.edge("tsqrt_2", "tsmqr_25")


#Add edges for the third tile-row update
dot.edge("tsmqr_22", "tsmqr_32")
dot.edge("tsqrt_3", "tsmqr_32")
dot.edge("tsmqr_23", "tsmqr_33")
dot.edge("tsmqr_24", "tsmqr_34")
dot.edge("tsqrt_3", "tsmqr_34")
dot.edge("tsmqr_25", "tsmqr_35")
dot.edge("tsqrt_3", "tsmqr_35")

#Add edges for the fourth tile-row update
dot.edge("tsmqr_32", "tsmqr_42")
dot.edge("tsqrt_4", "tsmqr_42")
dot.edge("tsmqr_33", "tsmqr_43")
dot.edge("tsqrt_4", "tsmqr_43")
dot.edge("tsmqr_34", "tsmqr_44")
dot.edge("tsqrt_4", "tsmqr_44")
dot.edge("tsmqr_35", "tsmqr_45")
dot.edge("tsqrt_4", "tsmqr_45")

#Add edges for the fourth tile-row update
dot.edge("tsmqr_42", "tsmqr_52")
dot.edge("tsqrt_5", "tsmqr_52")
dot.edge("tsmqr_43", "tsmqr_53")
dot.edge("tsqrt_5", "tsmqr_53")
dot.edge("tsmqr_44", "tsmqr_54")
dot.edge("tsqrt_5", "tsmqr_54")
dot.edge("tsmqr_45", "tsmqr_55")
dot.edge("tsqrt_5", "tsmqr_55")

#Add edges leading to the first LQ
# dot.edge("tsmqr_52", "lq_1")
# dot.edge("tsmqr_53", "lq_1")
# dot.edge("tsmqr_54", "lq_1")
# dot.edge("tsmqr_55", "lq_1")

#Save the file
dot.render("../fig/dag_better")
dot.view()
