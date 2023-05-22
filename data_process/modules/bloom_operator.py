from pybloom_live import ScalableBloomFilter, BloomFilter
import pandas as pd
import glob

class BloomOperator:
    # 可自动扩容的布隆过滤器
    bloom = ScalableBloomFilter(initial_capacity=100000, error_rate=0.001)
    def __init__(self):
        pass        
    def check(self, href):
        # 检查href是否存在于布隆过滤器中
        return href in self.bloom

    def insert(self, href):
        # 将新href插入布隆过滤器
        self.bloom.add(href) 