docker build -f ./Dockerfile_porn_detection_lstm -t porn_detection_lstm:1.0 .
docker rm -f porn_detection_lstm
docker run -itd --name porn_detection_lstm -p 9021:9000 porn_detection_lstm:1.0
docker logs porn_detection_lstm
docker diff porn_detection_lstm

#没问题的话就可以执行推送命令
docker tag porn_detection_lstm:1.0 registry.cn-shenzhen.aliyuncs.com/duolabmeng/porn_detection_lstm:1.1
docker push registry.cn-shenzhen.aliyuncs.com/duolabmeng/porn_detection_lstm:1.1


