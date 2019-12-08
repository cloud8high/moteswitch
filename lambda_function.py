import requests
import time

def notify_to_match():
    url = "https://fcm.googleapis.com/fcm/send"
    payload = '{ \
        "notification" : { \
            "title": "マッチングが成立しました！", \
            "body": "メッセージを送りましょう", \
            "sound":"default", \
            "icon":"@android:drawable/sym_action_chat",\
            "color":"#FF8000" \
        } , \
        "to" : "＜トークン＞", \
        "priority":"high" \
        }'.encode("utf-8")
    headers = {
        'Authorization': "key=＜APIキー＞",
        'Content-Type': "application/json",
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)

def lambda_handler(event, context):
    for i in range(100):
        notify_to_match()
        time.sleep(0.1)