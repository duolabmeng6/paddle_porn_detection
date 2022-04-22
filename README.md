# 快速部署色情文本检测

大家可以通过本项目提供的镜像，快速发布成可调用的Restful API服务。

# porn_detection_lstm

[使用模型 porn_detection_lstm](https://github.com/PaddlePaddle/PaddleHub/tree/release/v2.2/modules/text/text_review/porn_detection_lstm)

| 模型名称            |  senta_bilstm  |
| :------------------ | :------------: |
| 类别                | 文本-文本审核  |
| 网络                |      LSTM      |
| 数据集              | 百度自建数据集 |
| 是否支持Fine-tuning |       否       |
| 模型大小            |       1M       |
| 最新更新日期        |   2021-02-26   |
| 数据指标            |       -        |


# 部署方法

# 1. 在阿里云函数计算应用中心里立即创建

[阿里云Serverless 应用中心一键体验 ](https://fcnext.console.aliyun.com/applications/create?template=paddlePornDetection)

# 2. 终端上输入命令创建

```shell

s init paddlePornDetection  # 初始化项目
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

# 常用命令
```shell
s cli registry login # 登录授权 一次就行
s cli registry publish # 发布包
s cli registry list # 查看子机已发布的包

s init paddlePornDetection # 自己测试应用的效果
s deploy # 部署项目试试
```