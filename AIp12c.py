from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import(
    InvalidSignatureError
)
from linebot.models import *

app=Flask(__name__)  # __name__ 代表目前執行的模組

# Channel Access Token
line_bot_api = LineBotApi("Nr6mCIsNGslpKJagqwGXYLetpQx0UF2bfmvDAupvFIMmZ/ntSDWrVcRAPOI+OUeklrEWYaU96foNY0rOD+4wXNNPkvAKVGdFbXkcu3r9fblG+zBFT7dx4wjhXksPINOC4G3q6XffuRn/WDIJXoXNEQdB04t89/1O/w1cDnyilFU=")  #-- YOUR_CHANNEL_ACCESS_TOKEN
# Channel Secret
handler = WebhookHandler("48f6b1096e13a1d04269785c75363a8c")  #-- YOUR_CHANNEL_SECRET

# 監聽所有來自 /callback 的 Post Request 
@app.route("/callback", methods=['POST']) 
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print(">>>>>>>>> testing-body:",body)
    # handle webhook body
    try:
        print(">>>>>>>>> testing-try:...")
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    text = event.message.text
    if (text=="Hi"):
        reply_text = "Hello"
        #Your user ID
    elif(text=="你好"): 
        reply_text = ""
    elif(text=="機器人"):
        reply_text = ""
    else:  # 如果非以上的選項，就會學你說話
        reply_text = text

    message = TextSendMessage(reply_text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
