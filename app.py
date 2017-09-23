# encoding: utf-8
from  import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
#import pyodbc

#server = 'digitaleco.database.windows.net'
#database ='Digital_ECO'
#username = 'anuwatk'
#password = 'L@nnacom@1'
#driver = '{SQL Server}'
#cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
#cursor = cnxn.cursor()
#cursor.execute("SELECT [ID],[username],[contact] FROM [dbo].[Alluser]")
#row = cursor.fetchone()
#while row:
  #  print (str(row[0]) + " " + str(row[1]))
  #  row = cursor.fetchone()

app = Flask(__name__)

line_bot_api = LineBotApi('N1GTeUQXeB77zQpSTKeoprctXQDZI1OQPAJNfuDZVHgUHBEeY2zPQXiLG7dOhFodGwCu1PXFv+bY/wDAODAFN+rpKMLoQaUYjJGdxNIMWGcOMy7sbNjv8mDcMrFSw4HpMn2VmSR0s+CgY4kHc7BMDwdB04t89/1O/w1cDnyilFU=') #Your Channel Access Token
handler = WebhookHandler('b99029980da84da3980d785cf5737d63') #Your Channel Secret

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    #text = event.message.text + str(row[0]) + " " + str(row[1])  #message from user
    text = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text)) #reply the same message from user
    

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])