import numpy as np
import pandas as pd
import json

class tweetAnalysis:
    # コンストラクタの引数としてtweetのデータが格納されているjsonファイルのパス
    def __init__(self, filePath):
        # Twitterからデータをとれた場合を想定したデータを取得
        self.filePath = filePath
        f = open(self.filePath, "r", encoding="utf-8")
        res = json.load(f)

        # json --> pandas.DataFrame
        data = []
        for line in res["statuses"]:
            data.append([line["id"], line["created_at"], line["text"], line["user"]["name"], line["user"]["description"],
                        line["user"]["followers_count"], int(line["user"]["friends_count"]), line["user"]["verified"],
                        line["user"]["listed_count"], line["favorite_count"], line["retweet_count"]])

        self.df = pd.DataFrame(data,
                    columns=["id", "time", "text", "username", "description", "followers_count", "friends_count", "verified", "listed_count", "favorite_count", "retweet_count"])

        # str型から適切な型へ変換
        self.df = self.df.astype({"followers_count" : int})
        self.df = self.df.astype({"friends_count" : int})
        self.df = self.df.astype({"verified" : bool})
        self.df = self.df.astype({"listed_count" : int})
        self.df = self.df.astype({"favorite_count" : int})
        self.df = self.df.astype({"retweet_count" : int})

    # 文字列に「です」「ます」がいくつ含まれるかを返す
    def countDesuMasu(self, str):
        desu_count = str.count("です")
        masu_count = str.count("ます")
        return desu_count + masu_count

    # 正規化するための関数
    def normalize(self, x, min_x, max_x):
        return (x - min_x) / (max_x - min_x)
    
    def calculateEvaluationValue(self):
        # 各特徴量の上限値の定義
        max_favorite_count = 200
        max_ff_rate = 500.0
        max_listed_count = 1100

        # フォロワー数とフォロー数の比
        self.df["ff_rate"] = self.df["followers_count"] / self.df["friends_count"]
        # プロフィールの文字数
        self.df["description_word_count"] = self.df["description"].apply(lambda x : len(x))
        # ツイート本文の文字数
        self.df["text_word_count"] = self.df["text"].apply(lambda x : len(x))
        # プロフィールの「です」「ます」の数
        self.df["description_DesuMasu_count"] = self.df["description"].apply(lambda x : self.countDesuMasu(x))

        # 正規化（上限値あり）
        self.df["normalized_favorite_count"] = self.df["favorite_count"] / max_favorite_count
        self.df.normalized_favorite_count = self.df.normalized_favorite_count.where(self.df.normalized_favorite_count < 1, 1)
        self.df["normalized_ff_rate"] = self.df["ff_rate"] / max_ff_rate
        self.df.normalized_ff_rate = self.df.normalized_ff_rate.where(self.df.normalized_ff_rate < 1, 1)
        self.df["normalized_listed_count"] = self.df["listed_count"] / max_listed_count
        self.df.normalized_listed_count = self.df.normalized_listed_count.where(self.df.normalized_listed_count < 1, 1)

        # 正規化（上限値なし）
        self.df["normalized_text_word_count"] = self.df["text_word_count"].apply(lambda x : self.normalize(x, self.df["text_word_count"].max(), self.df["text_word_count"].min()))
        self.df["normalized_retweet_count"] = self.df["retweet_count"].apply(lambda x : self.normalize(x, self.df["retweet_count"].max(), self.df["retweet_count"].min()))

        # 評価値 まだ検討中
        self.df["point"] = 7*self.df["normalized_favorite_count"] + 5*self.df["normalized_ff_rate"] + 4.5*self.df["listed_count"] + 3.5*self.df["normalized_retweet_count"] + 10*self.df["verified"]

    def outputCsvFile(self):
        self.df.to_csv("tweet_data.csv", index=False)# test

    # dataframeを加工して評価値を計算したので，初期化
    def initializeTweetDataFrame(self):
        f = open(self.filePath, "r", encoding="utf-8")
        res = json.load(f)

        # json --> pandas.DataFrame
        data = []
        for line in res["statuses"]:
            data.append([line["id"], line["created_at"], line["text"], line["user"]["name"], line["user"]["description"],
                        line["user"]["followers_count"], int(line["user"]["friends_count"]), line["user"]["verified"],
                        line["user"]["listed_count"], line["favorite_count"], line["retweet_count"]])

        self.df = pd.DataFrame(data,
                    columns=["id", "time", "text", "username", "description", "followers_count", "friends_count", "verified", "listed_count", "favorite_count", "retweet_count"])
    
# インスタンスの生成
tA = tweetAnalysis("testData.json")
tA.calculateEvaluationValue()
tA.outputCsvFile()
# tA.initializeTweetDataFrame()
# tA.outputCsvFile()