import paddlehub as hub

porn_detection_lstm = hub.Module(name="porn_detection_lstm")

test_text = ["黄片下载", "打击黄牛党","黄片下载打击黄牛党"]

results = porn_detection_lstm.detection(texts=test_text, use_gpu=False, batch_size=1)

for index, text in enumerate(test_text):
    results[index]["text"] = text
for index, result in enumerate(results):
    print(results[index])

# 输出结果如下：
# {'text': '黄片下载', 'porn_detection_label': 1, 'porn_detection_key': 'porn', 'porn_probs': 0.9879, 'not_porn_probs': 0.0121}
# {'text': '打击黄牛党', 'porn_detection_label': 0, 'porn_detection_key': 'not_porn', 'porn_probs': 0.0004, 'not_porn_probs': 0.9996}