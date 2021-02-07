# -*- coding: utf-8 -*-
# python 3.7

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import pandas as pd
from requests_oauthlib import OAuth1Session

# EvaluateFunction class のインポート
import evaluationFunction as EvalFunc

# Static Final Param
KEYWORD = "#コロナ"
TWEET_NUM = 50



def FireStore_Write(mDF, keyword):
    # FireStoreプロジェクトの秘密鍵を発行して，秘密鍵の入ったJSONを指定
    cred = credentials.Certificate("hackathon-project-fe887-firebase-adminsdk-hvct6-4370fb58c5.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    for i in range(0,len(mDF)):
        Docs_name = str(mDF["id"][i]) # idをドキュメント名に代用
        doc_ref = db.collection(keyword).document(Docs_name)
        doc_ref.set({
            "id":                   int(mDF["id"][i]),
            "text":                 mDF["text"][i],
            "time":                 mDF["time"][i],
            "username":             mDF["username"][i],
            "verified":             bool(mDF["verified"][i]),
            "description":          mDF["description"][i],

            "profile_image_url":    mDF["profile_image_url"][i],
            "profile_banner_url":   mDF["profile_banner_url"][i],
            
            "favorite_count":       int(mDF["favorite_count"][i]),
            "followers_count":      int(mDF["followers_count"][i]),
            "friends_count":        int(mDF["friends_count"][i]),
            "retweet_count":        int(mDF["retweet_count"][i]),
            "point":                int(mDF["point"][i]),
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
        'q':        keyWord,
        'exclude':  'retweets',#RTを除外
        'lang':     'ja',
        'count':    tweetNum,
    }
    res = api.get(url, params=params)
    return json.loads(res.text)


def main():
    # ツイートを取得し，JSONを辞書型に変換してもらう
    res = TweetDataGet(KEYWORD, TWEET_NUM)

    # インスタンスの生成
    tA = EvalFunc.tweetAnalysis(res)
    tA.calculateEvaluationValue()
    # tA.outputCsvFile()
    # tA.initializeTweetDataFrame()
    # tA.outputCsvFile()
    
    # test
    tA.df.to_csv("tweet_data.csv", index=False)

    # firestore_write
    FireStore_Write(tA.df,KEYWORD)

    return


if __name__ == "__main__":
    
    main()
