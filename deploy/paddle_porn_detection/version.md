# 快速部署色情文本检测

大家可以通过本项目提供的镜像，快速发布成可调用的Restful API服务。

# 部署方法

# 1. 在阿里云函数计算应用中心里立即创建

# 2. 终端上输入命令创建

```shell

s init paddle_porn_detection  # 初始化项目
s deploy  # 部署项目

```

# 调用方法

```python
import requests
import json

def getResult(text):
    data = {"texts": text, "batch_size": 1, "use_gpu":False}
    r = requests.post("http://127.0.0.1:9021/predict/porn_detection_lstm",
                      headers={"Content-Type": "application/json"}, data=json.dumps(data))
    return json.dumps(r.json(), indent=4, ensure_ascii=False)

print(getResult(["黄片下载", "打击黄牛党"]))


# 输出结果如下：
# {'text': '黄片下载', 'porn_detection_label': 1, 'porn_detection_key': 'porn', 'porn_probs': 0.9879, 'not_porn_probs': 0.0121}
# {'text': '打击黄牛党', 'porn_detection_label': 0, 'porn_detection_key': 'not_porn', 'porn_probs': 0.0004, 'not_porn_probs': 0.9996}

```

# 本应用的镜像开发教程

https://github.com/duolabmeng6/paddlehub_ppocr

阅读本文你将学会：

在 Serverless 架构中 docker 镜像制作的最佳实践，游刃有余的部署复杂场景下的深度学习模型

熟练的使用各厂商提供的 Serverless 服务，部署。

制作小巧精良的 docker 镜像