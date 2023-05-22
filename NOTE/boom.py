from bitarray import bitarray
from bloomfilter import BloomFilter

# 初始化一个布隆过滤器,容量为1000,错误率为0.1% 
bf = BloomFilter(100000, 0.001)  

# 添加元素到过滤器
bf.add("a")
bf.add("b")
bf.add("c")

# 检查元素是否存在
bf.add("a")   # True
bf.add("d")   # False (可能存在误判)

# 获取过滤器信息
len(bf)     # 100000 
bf.count("a")  # 1
bf.false_positive_probability()  # 0.001