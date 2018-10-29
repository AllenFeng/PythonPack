
#导入库函数
from bokeh.charts import Bar, output_file, show
#在电脑屏幕上使用 output_notebook来可视化数据
#准备数据 (模拟数据)
data = {"y": [1, 2, 3, 4, 5]}
#输出到Line.HTML
output_file("lines.html", title="line plot example")
#创建一个新的含有标题和轴标签的窗口在线窗口
p = Bar(data, title="Line Chart Example", xlabel='x', ylabel='values', width=400, height=400)
#显示结果
show(p)
