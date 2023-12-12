import matplotlib.pyplot as plt
import numpy as np
# 假设数据
years = np.arange(2006, 2023)
data_100Mb = [0.38, 0.20, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.05, 0, 0, 0, 0, 0, 0, 0]
data_1000Mb = [0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.1, 0.1, 0.05, 0, 0, 0, 0, 0, 0, 0]
# data_10Gb = np.random.rand(len(years)) * 0.5 + data_1000Mb
# data_40Gb = np.random.rand(len(years)) * 0.6 + data_10Gb
# 创建堆叠面积图
plt.fill_between(years, data_1000Mb, color="green", label="1000Mb")
plt.fill_between(years, data_100Mb, color="red", label="100Mb")
# plt.fill_between(years, data_10Gb, color="blue", label="10Gb")
# plt.fill_between(years, data_40Gb, color="purple", label="40Gb")
# 添加标题和标签
plt.title('网络电力使用预测')
plt.xlabel('年份')
plt.ylabel('网络电力使用 (十亿千瓦时)')
# 添加图例
plt.legend(loc="upper left")
# 添加网格线
plt.grid(True)
# 保存图像
#plt.savefig('network_usage_forecast.png')
# 显示图像
plt.show()
