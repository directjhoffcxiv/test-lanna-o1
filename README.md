# line-bot-python-heroku
***
API : [https://devdocs.line.me/en/](https://devdocs.line.me/en/)  
line-bot-sdk-python : [https://github.com/line/line-bot-sdk-python](https://github.com/line/line-bot-sdk-python)  
Fixie : [https://elements.heroku.com/addons/fixie](https://elements.heroku.com/addons/fixie)
***

1.Line Messaging API  
[https://business.line.me/zh-hant/services/bot](https://business.line.me/zh-hant/services/bot)  
 - ใส่ Channel Access Token``Channel Secret`

2. Deploy Heroku 
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/abechen/line-bot-python-heroku)

3.app.py
`line_bot_api = LineBotApi('') #Your Channel Access Token`  
`handler = WebhookHandler('') #Your Channel Secret` 

4. Add-ons Fixie  
[https://elements.heroku.com/addons/fixie](https://elements.heroku.com/addons/fixie) 

5. Line developers `Webhook URL`  
`https://{YOUR_HEROKU_SERVER_ID}.herokuapp.com/callback`