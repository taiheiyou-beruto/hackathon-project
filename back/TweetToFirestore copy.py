# -*- coding: utf-8 -*-
# python 3.7

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import pandas as pd
from requests_oauthlib import OAuth1Session

KEYWORD = "#コロナ"
TWEET_NUM = 10

def FireStore_Write(mDF, keyword):
    # FireStoreプロジェクトの秘密鍵を発行して，秘密鍵の入ったJSONを指定
    cred = credentials.Certificate("hackathon-project-fe887-firebase-adminsdk-hvct6-4370fb58c5.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    for i in range(0,len(mDF)):
        Docs_name = str(mDF["id"][i]) # idをドキュメント名に代用
        doc_ref = db.collection(keyword).document(Docs_name)
        doc_ref.set({
            'id':                   int(mDF["id"][i]),
            'text':                 mDF["text"][i],
            'time':                 mDF["time"][i],
            'username':             mDF["username"][i],
            'verified':             bool(mDF["verified"][i]),
            'favorite_count':       int(mDF["favorite_count"][i]),

            "profile_image_url":    mDF["profile_image_url"][i],
            "profile_banner_url":   mDF["profile_banner_url"][i],
            
            'hoge_point':           int(mDF["point"][i]), # test
        })

###
# keyWord  : 検索キーワード
# TweetNum : ツイートの取得件数
###
def TweetDataGet(keyWord, tweetNum):
    # # トークン情報
    CK      = "**"
    CKS     = "**"
    AT      = "**"
    ATS     = "**"
    # OAuth認証
    api = OAuth1Session(CK, CKS, AT, ATS)

    url = 'https://api.twitter.com/1.1/search/tweets.json?tweet_mode=extended'
    params = {
        'q': keyWord,
        'exclude': 'retweets',#RTを除外
        'count': tweetNum,
    }
    res = api.get(url, params=params)
    return json.loads(res.text)



if __name__ == "__main__":
    res = TweetDataGet(KEYWORD, TWEET_NUM)

    # json --> pandas.DataFrame
    data = []
    for line in res["statuses"]:
        # バナー画像をつけていない人もいるので，その場合は"no setting" と書きます
        if ("profile_banner_url" not in line["user"].keys()):
            line["user"]["profile_banner_url"] = "no setting"

        data.append([line["id"], line["full_text"], line["created_at"], line["user"]["name"], line["user"]["description"],
                     line["user"]["followers_count"], line["user"]["friends_count"], line["user"]["verified"],
                     line["user"]["profile_image_url_https"], line["user"]["profile_banner_url"], 
                     line["user"]["listed_count"], line["favorite_count"]])
    
    df = pd.DataFrame(data,
                  columns=["id", "text", "time", "username", "description", "follower", "friend_count", "verified", 
                            "profile_image_url", "profile_banner_url", "listed_count", "favorite_count"] )
    
    # 評価式ができ次第，DataFrameに評価値の列を設けて格納
    df["point"] = 0.001 * df["follower"] + 0.01 * df["friend_count"] # test

    df.to_csv("tweet_data.csv", index=False)# test

    FireStore_Write(df,KEYWORD)
