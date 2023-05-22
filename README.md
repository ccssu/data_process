# data_process
构建process_demo

```shell
data_process/
├── download.py         # 下载视频脚本 
├── detect_language.py  # 语言检测脚本
├── get_clip_feature.py # 获取视频CLIP特征脚本 
├── filter_data.py      # 根据CLIP计算过滤无关数据
├── build_dataset.py    # 构建数据集脚本
├── config.yaml         # 配置文件
└── data               # 数据目录
    ├── raw            # 下载的原始视频
    ├── clips          # 剪辑过的视频
    ├── features       # 视频特征    
    ├── drop           # 被过滤的数据
    └── dataset        # 构建的最终数据集


data_process/
├── README.md         # 项目说明文档
├── requirements.txt  # 依赖包列表
├── LICENSE           # 许可证
├── setup.py          # 打包配置文件(如果需要)
├── src/              # 源代码目录
│   ├── __init__.py   # 使 src 成为一个包
│   ├── main.py       # 程序入口文件
│   ├── utils.py      # 工具函数
│   ├── config.py     # 工具函数
│   └── modules/      # 模块目录
│       ├── __init__.py
│       ├── detect_language.py  # 语言检测脚本
│       ├── get_clip_feature.py # 获取CLIP特征脚本 
│       ├── download.py         # 下载脚本 
│       ├── build_dataset.py    # 构建数据集脚本
│       ├── detect_language.py  # 语言检测脚本
│       └── filter_data.py      # 根据CLIP计算过滤无关数据
|     
├── test/              # 测试目录
│   └── test_*.py    
└── data/              # 数据目录
    ├── raw            # 下载的原始视频
    ├── clips          # 剪辑过的图像
    ├── drop           # 被过滤的数据
    ├── dataset        # 构建的最终数据集
    └── download_log   # 下载日志,记录下载过的URL
```


语言检测工具   https://pypi.org/project/lingua-language-detector/
