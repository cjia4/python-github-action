import logging
import logging.handlers
import os
import requests
import json
import time
#https://open.dingtalk.com/document/orgapp/types-of-messages-sent-by-robots

import datetime
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    DINGDING_WEBHOOK = os.environ["DINGDING"]
except KeyError:
    DINGDING_WEBHOOK = "Token not available!"
    logger.info("Token not available!")
    #raise


if __name__ == "__main__":
    logger.info(f"Token value: {DINGDING_WEBHOOK}")

    contents = "嘟嘟:这是来自github action的消息"

    #print(ticks_1)
    # 更改为自己的钉钉机器人
    baseUrl = DINGDING_WEBHOOK
    now = str(datetime.datetime.now())
    # please set charset= utf-8
    HEADERS = {
        "Content-Type": "application/json ;charset=utf-8 "
    }
    # 这里的message是你想要推送的文字消息
    message = "时间：" + now + "\n" + contents
    stringBody = {
        "msgtype": "text",
        "text": {"content": message},
        "at": {
            "atMobiles": [""],
            "isAtAll": "false"  # @所有人 时为true，上面的atMobiles就失效了
        }
    }
    MessageBody = json.dumps(stringBody)
    result = requests.post(url=baseUrl, data=MessageBody, headers=HEADERS)
    print(result.text)
    
