import numpy as np
import pandas as pd
import json
import datetime

class tweetAnalysis:
    # コンストラクタの引数にjsonファイルのパス
    def __init__(self, filePath):
        # Twitterからデータをとれた場合を想定したデータを取得
        self.filePath = filePath
        f = open(self.filePath, "r", encoding="utf-8")
        res = json.load(f)

        # json --> pandas.DataFrame
        data = []
        for line in res["statuses"]:
            data.append([line["id"], line["user"]["created_at"], line["full_text"], line["user"]["name"], line["user"]["description"],
                        line["user"]["followers_count"], line["user"]["friends_count"], line["user"]["verified"],
                        line["user"]["listed_count"], line["favorite_count"], line["retweet_count"], line["user"]["statuses_count"]])

        self.df = pd.DataFrame(data,
                    columns=["id", "time", "text", "username", "description", "followers_count", "friends_count", "verified", "listed_count", "favorite_count", "retweet_count", "statuses_count"])

        # str型から適切な型へ変換
        self.df = self.df.astype({"followers_count" : int})
        self.df = self.df.astype({"friends_count" : int})
        self.df = self.df.astype({"verified" : bool})
        self.df = self.df.astype({"listed_count" : int})
        self.df = self.df.astype({"favorite_count" : int})
        self.df = self.df.astype({"retweet_count" : int})

    # 文字列に「です」「ます」などがいくつ含まれるかを返す
    def count_word(self, str):
        words = ["です", "ます", "公式", "アカウント", "情報"] # 非デマの傾向が強いワード
        wordCount = 0
        for word in words:
            wordCount += str.count(word)
        return wordCount

    def count_PN_word(self, str):
        positive = ["愉快な", "面白い", "楽しい", "嬉しい", "喜ばしい", "誇らしい", "清々しい", "陽気な", "快調な", "爽やかな", "機嫌良い", "元気な", "生き生き", "うきうき", "わくわく", "快い", "心地よい", "微笑ましい", "麗しい", "気持ちいい", "穏やかな", "落ち着いた", "長閑な", "安らいだ", "快適な", "和やかな"]
        negative = ["不愉快な", "不快な", "腹立たしい", "忌忌しい", "忌まわしい", "苛立たしい", "もどかしい", "歯痒い", "ひどい", "憤怒", "腹立ち", "立腹", "いらいら", "胸くそ悪い", "馬鹿らしい", "むっとした", "かっとした", "むしゃくしゃした", "憎らしい", "鬱陶しい", "煩わしい", "苦い", "苦々しい", "悔しい", "情けない", "恨めしい", "怖い", "恐ろしい", "おっかない", "はらはら", "怪しい", "解せない", "訝しい", "重苦しい", "物憂い", "さみしい", "悲しい", "切ない", "苦しい", "辛い", "やるせない", "悩ましい", "憂い", "やりきれない", "いたたまれない", "狂おしい", "心細い", "心許せない", "気味悪い", "おろおろ", "くよくよ", "不安な", "気がかりな", "沈んだ", "悲観した", "胡散臭い", "無気力な", "ぼんやりした", "退屈な", "だるい", "つまらない"]
        positiveCount = 0
        negativeCount = 0
        for p in positive:
            positiveCount += str.count(p)
        
        for n in negative:
            negativeCount += str.count(n)
        return positiveCount - negativeCount

    # 正規化するための関数
    def normalize(self, x, min_x, max_x):
        # 例外処理
        if(max_x == min_x):
            return 0
        return (x - min_x) / (max_x - min_x)
    
    def normalize_column(self, columnName):
        new_columnName = "normalized_" + columnName # 実装時は不必要
        maximum = self.df[columnName].max() # 最大値
        minimum = self.df[columnName].min() # 最小値
        self.df[new_columnName] = self.df[columnName].apply(lambda x : self.normalize(x, minimum, maximum))

    def normalize_column_withUpper(self, columnName, upperLimit):
        new_columnName = "normalized_" + columnName # 実装時は不必要
        minimum = self.df[columnName].min() # 最小値
        self.df[new_columnName] = self.df[columnName].apply(lambda x : self.normalize(x, minimum, upperLimit))
        self.df[new_columnName] = self.df[new_columnName].where(self.df[new_columnName] < 1, 1)

    def standardize(self, x, mu, sigma):
        if sigma == 0:
            return 1.
        return (x-mu) / sigma * 10 + 50

    # 値の偏差値を計算 評価値を偏差値かする時に使用
    def standardize_column(self, columnName):
        mu    = self.df[columnName].mean() # 平均値
        sigma = self.df[columnName].std()  # 標準偏差
        self.df[columnName] = self.df[columnName].apply(lambda x : self.standardize(x, mu, sigma))

    # アカウント作成時からアカウント年齢を計算 (日数)
    def calculateAccountAge(self, str):
        month_dict = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}
        year  = int(str[len(str)-4:len(str)])
        month = month_dict[str[4:7]]
        day   = int(str[8:10])
        created_at = datetime.date(year, month, day)
        dt_now = datetime.date.today()
        return (dt_now-created_at).days

    # 評価値を算出
    def calculateEvaluationValue(self):
        # 各特徴量の上限値の定義
        upper_favorite_count = 200
        upper_ff_rate = 500.0
        upper_listed_count = 1100
        upper_followers_count = 3000
        upper_text_word_count = 140
        upper_retweet_count = 10000
        upper_statuses_count = 2000
        upper_description_word_count = 160
        upper_account_age = 365
        upper_PN_word_count = 5

        # フォロワー数とフォロー数の比
        # その前に前処理として，フォロー数が0だと比を出せないので，フォロー数が0のときは1とする．
        self.df["friends_count"] = self.df["friends_count"].where(self.df["friends_count"] != 0, 1)
        self.df["ff_rate"] = self.df["followers_count"] / self.df["friends_count"]
        # プロフィールの文字数
        self.df["description_word_count"] = self.df["description"].apply(lambda x : len(x))
        # ツイート本文の文字数
        self.df["text_word_count"] = self.df["text"].apply(lambda x : len(x))
        # プロフィールの「です」「ます」の数
        self.df["description_DesuMasu_count"] = self.df["description"].apply(lambda x : self.count_word(x))
        # アカウントが作られてからの日数を計算
        self.df["account_age"] = self.df["time"].apply(lambda str : self.calculateAccountAge(str))
        # 文章の感情を表す指数
        self.df["PN_word_count"] = self.df["text"].apply(lambda str : self.count_PN_word(str))

        # 正規化（上限値あり）
        # https://www.datarobot.com/jp/blog/datarobot-finds-false-rumors-on-sns/ より上限値がわかる場合，こちらを採用
        self.normalize_column_withUpper("favorite_count", upper_favorite_count)
        self.normalize_column_withUpper("ff_rate", upper_ff_rate)
        self.normalize_column_withUpper("listed_count", upper_listed_count)
        self.normalize_column_withUpper("followers_count", upper_followers_count)
        self.normalize_column_withUpper("text_word_count", upper_text_word_count)
        self.normalize_column_withUpper("retweet_count", upper_retweet_count)
        self.normalize_column_withUpper("statuses_count", upper_statuses_count) # 総ツイート数
        self.normalize_column_withUpper("description_word_count", upper_description_word_count)
        self.normalize_column_withUpper("account_age", upper_account_age)
        self.normalize_column_withUpper("PN_word_count", upper_PN_word_count)

        # 正規化（上限値なし）
        # 抽出したツイートに依存する相対的な値ではなく，絶対的な値にするためにすべての上限値を指定し正規化した

        # 評価値 まだ検討中
        self.df["point"] = 7   * self.df["normalized_favorite_count"] \
                         + 5   * self.df["normalized_ff_rate"] \
                         + 5   * self.df["normalized_followers_count"] \
                         + 4.5 * self.df["normalized_listed_count"] \
                         + 3.5 * self.df["normalized_retweet_count"] \
                         + 30  * self.df["verified"] \
                         + 3.4 * self.df["normalized_account_age"] \
                         + 3   * self.df["normalized_statuses_count"] \
                         - 2.0 * self.df["normalized_text_word_count"] \
                         + 1.0 * self.df["normalized_PN_word_count"]

        self.standardize_column("point") # 非デマ度（評価値）を偏差値として出力

        self.df = self.df.sort_values('point', ascending=False) # 評価値の大きい順に並び替え (降順)

    # data frameのcsv出力
    def outputCsvFile(self):
        self.df.to_csv("tweet_data.csv", index=False)# test

    # dataframeを初期化
    def initializeTweetDataFrame(self):
        f = open(self.filePath, "r", encoding="utf-8")
        res = json.load(f)

        # json --> pandas.DataFrame
        data = []
        for line in res["statuses"]:
            data.append([line["id"], line["user"]["created_at"], line["full_text"], line["user"]["name"], line["user"]["description"],
                        line["user"]["followers_count"], line["user"]["friends_count"], line["user"]["verified"],
                        line["user"]["listed_count"], line["favorite_count"], line["retweet_count"], line["user"]["statuses_count"]])

        self.df = pd.DataFrame(data,
                    columns=["id", "time", "text", "username", "description", "followers_count", "friends_count", "verified", "listed_count", "favorite_count", "retweet_count", "statuses_count"])

if __name__ == "__main__":
    # インスタンスの生成
    tA = tweetAnalysis("test_new.json")
    tA.calculateEvaluationValue()
    tA.outputCsvFile()

    # tA.outputCsvFile()
    # tA.initializeTweetDataFrame()