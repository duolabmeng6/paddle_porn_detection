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