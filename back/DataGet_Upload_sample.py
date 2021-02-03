# -*- coding: utf-8 -*-
# python 3.6

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import json
import pandas as pd

def FireStore_Write(mDF):
    # FireStoreプロジェクトの秘密鍵を発行して，秘密鍵の入ったJSONを指定
    cred = credentials.Certificate("fireStore_taiheiyou_cred.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    for i in range(0,len(mDF)):
        Docs_name = str(mDF["id"][i]) # idをドキュメント名に代用
        doc_ref = db.collection(u'tweet').document(Docs_name)
        doc_ref.set({
            'id':            int(mDF["id"][i]),
            'time':          mDF["time"][i],
            'text':          mDF["text"][i],
            'username':      mDF["username"][i],
            'description':   mDF["description"][i],
            'follower':      int(mDF["follower"][i]),
            'friend_count':  int(mDF["friend_count"][i]),
            'verified':      bool(mDF["verified"][i]),
            'hoge_point':    int(mDF["point"][i]), # test
        })


if __name__ == "__main__":
    # Twitterからデータをとれた場合を想定したデータを取得
    filePath = "testData.json"
    f = open(filePath, "r", encoding="utf-8")
    res = json.load(f)

    # json --> pandas.DataFrame
    data = []
    for line in res["statuses"]:
        data.append([line["id"], line["created_at"], line["text"], line["user"]["name"], line["user"]["description"],
                     line["user"]["followers_count"], line["user"]["friends_count"], line["user"]["verified"]])
    df = pd.DataFrame(data,
                  columns=["id", "time", "text", "username", "description", "follower", "friend_count", "verified"])
    
    # 評価式ができ次第，DataFrameに評価値の列を設けて格納
    df["point"] = 0.001 * df["follower"] + 0.01 * df["friend_count"] # test

    FireStore_Write(df)

    df.to_csv("tweet_data.csv", index=False)# test