# paddlePornDetection 帮助文档

<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=paddlePornDetection&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=paddlePornDetection" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=paddlePornDetection&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=paddlePornDetection" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=paddlePornDetection&type=packageDownload">
  </a>
</p>

<description>

> ***本应用基于百度开源的 PaddlePaddle 项目，可以快速实现色情文本检测服务***

</description>

<table>

## 前期准备
使用该项目，推荐您拥有以下的产品权限 / 策略：

| 服务/业务 | 函数计算 |     
| --- |  --- |   
| 权限/策略 | AliyunFCFullAccess</br>AliyunContainerRegistryFullAccess |     


</table>

<codepre id="codepre">

# 代码 & 预览

- [:smiley_cat: 源代码](https://github.com/duolabmeng6/paddle_porn_detection)

        

</codepre>

<deploy>

## 部署 & 体验

<appcenter>

- :fire: 通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=paddlePornDetection) ，
[![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=paddlePornDetection)  该应用。 

</appcenter>

- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
    - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://www.serverless-devs.com/fc/config) ；
    - 初始化项目：`s init paddlePornDetection -d paddlePornDetection`   
    - 进入项目，并进行项目部署：`cd paddlePornDetection && s deploy -y`

</deploy>

<appdetail id="flushContent">

# 应用详情

## 调用方法

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

## 本应用的镜像开发教程

https://github.com/duolabmeng6/paddlehub_ppocr

阅读本文你将学会：

在 Serverless 架构中 docker 镜像制作的最佳实践，游刃有余的部署复杂场景下的深度学习模型

熟练的使用各厂商提供的 Serverless 服务，部署。

制作小巧精良的 docker 镜像

</appdetail>

<devgroup>

## 开发者社区

您如果有关于错误的反馈或者未来的期待，您可以在 [Serverless Devs repo Issues](https://github.com/serverless-devs/serverless-devs/issues) 中进行反馈和交流。如果您想要加入我们的讨论组或者了解 FC 组件的最新动态，您可以通过以下渠道进行：

<p align="center">

| <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407298906_20211028074819117230.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407044136_20211028074404326599.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407252200_20211028074732517533.png" width="130px" > |
|--- | --- | --- |
| <center>微信公众号：`serverless`</center> | <center>微信小助手：`xiaojiangwh`</center> | <center>钉钉交流群：`33947367`</center> | 

</p>

</devgroup>