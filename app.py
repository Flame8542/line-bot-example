import os
import json
from line_bot import LineBotApi, WebhookHandler
from line_bot.exceptions import InvalidSignatureError
from line_bot.models import MessageEvent, TextMessage, TextSendMessage

# 載入環境變數
LINE_CHANNEL_ACCESS_TOKEN = os.getenv('0wBpNe5fOX0TeeZGkSCL5CH6bJDry1O9lQzNxj3AKBHAm6dRTwGqkJ0ft7eAz7cYDfxgNs8vunZwSx5Jz73NzWCXL4Vq42JdqvhyBP5Cvy+IcwlGQT+6KEjSSfQKr6P7AmBU/aQyh2AWrCaKb1HMeAdB04t89/1O/w1cDnyilFU=')
LINE_CHANNEL_SECRET = os.getenv('3c6a0b0fb037654523461abb419275ba')

# 初始化 Line Bot API 與 Webhook Handler
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# 建立一個字典，用來儲存客戶名字和欠帳金額
customer_data = {}

def add_customer(name, amount_owed):
    """
    新增一個客戶並設定欠帳金額
    """
    customer_data[name] = amount_owed

def update_amount_owed(name, new_amount_owed):
    """
    更新客戶的欠帳金額
    """
    if name in customer_data:
        customer_data[name] = new_amount_owed
    else:
        print(f"客戶 {name} 不存在")

def get_amount_owed(name):
    """
    取得客戶的欠帳金額
    """
    if name in customer_data:
        return customer_data[name]
    else:
        print(f"客戶 {name} 不存在")

# 處理 Webhook 請求
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    if text == "新增客戶":
        add_customer("John Doe", 500)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="新增客戶 John Doe 成功，欠帳金額 500 元。")
        )
    elif text == "更新客戶欠帳":
        update_amount_owed("John Doe", 600)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="更新客戶 John Doe 的欠帳金額成功，目前欠帳金額 600 元。")
        )
    elif text == "查詢客戶欠帳":
        print(get_amount_owed("John Doe"))
        line_
