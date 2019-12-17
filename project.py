from flask import Flask, request, abort
from linebot import ( LineBotApi, WebhookHandler )
from linebot.exceptions import( InvalidSignatureError )
from linebot.models import *
import numpy as np 
import cv2

app = Flask(__name__)  # __name__ 代表目前執行的模組


line_bot_api = LineBotApi("HKMsq8V7VXcyU8IZeVMzAM2LEiiaLLR36GWRgIbcuVqq/cDth5KBIZLJ/re0b0ekP1lmNu2dYVvJgX3RGSiEQsvGJlN8dlf5mYHPned7jYsJpPysXd3r77+E2G5O6jzuMmiUvuhYjUEibVl4hZWiNQdB04t89/1O/w1cDnyilFU=")  #-- YOUR_CHANNEL_ACCESS_TOKEN

handler = WebhookHandler("13bb559d72a78209d8e02fadd0476a56")  #-- YOUR_CHANNEL_SECRET

@app.route("/callback", methods=['POST']) 
def callback():
    print(">>>>>>>>> 1.testing")  # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    print(">>>>>>>>> 2.testing")  # get request body as text
    body = request.get_data(as_text=True)
    print(">>>>>>>>> 3.testing"+body)
    app.logger.info("Request body: " + body)
    print(">>>>>>>>> 4.testing-body:"+body)
    # handle webhook body
    try:

        print(">>>>>>>>> 5.testing-try:...")

        print(">>>>>>>>> testing-1...")

        print(">>>>>>>>> 5.testing-try:...")

        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

###=== (5.5) 處理訊息  ===###
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
	
    for index in range(6):
      img[index] = cv2.imread('mc_picture'+str(index)+'.jpg')
		
    if event.message.id == "100001":
        return
    text = event.message.text
    if text == "100001":
        return
    if (text=="Hi"):
        reply_text = "Hello!要點餐推薦嗎"
        #Your user ID
    elif(text=="你好"): 
        reply_text = "Hello!要點餐推薦嗎"
    elif (text=="1" or text=="1號" or text=="大麥克" or text=="我要大麥克"):
        reply_text = "1號大麥克經典套餐$135\n推薦配可樂"
		picture = img[0] 
    elif (text=="2" or text=="2號" or text=="雙層牛肉吉事堡" or text=="我要雙層牛肉吉事堡"):
        reply_text = "2號雙層牛肉吉事堡經典套餐$125\n推薦配柳橙汁"
		picture = img[1]
    elif (text=="3" or text=="3號" or text=="安格斯黑牛堡" or text=="我要安格斯黑牛堡"):
        reply_text = "3號安格斯黑牛堡經典套餐$149\n推薦配奶茶"
		picture = img[2]
    elif (text=="4" or text=="4號" or text=="嫩煎雞腿堡" or text=="我要嫩煎雞腿堡"):
        reply_text = "4號嫩煎雞腿堡經典套餐$135\n推薦配咖啡"
		picture = img[3]
    elif (text=="5" or text=="5號" or text=="麥香雞" or text=="我要麥香雞"):
        reply_text = "5號麥香雞經典套餐$105\n推薦配冰紅茶"
		picture = img[4]
    elif (text=="6" or text=="6號" or text=="麥克雞塊(6塊)" or text=="麥克雞塊(6塊)"):
        reply_text = "6號麥克雞塊(6塊)經典套餐$119\n推薦配雪碧"
		picture = img[5]
    elif (text=="外送"):
        reply_text = "https://www.mcdelivery.com.tw/tw/home.html"
    elif (text=="菜單"):
        reply_text = "1號大麥克\n2號雙層牛肉吉事堡\n3號安格斯黑牛堡\n4號嫩煎雞腿堡\n5號麥香雞\n6號麥克雞塊(6塊)"
    else:  # 如果非以上的選項，就會學你說話
        reply_text = "不符合"
    message = TextSendMessage(reply_text)
    line_bot_api.reply_message(event.reply_token, message)
	message = TextSendMessage(picture)
	line_bot_api.reply_message(event.reply_token, message)

###=== (5.6) 執行程式  ===###
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)