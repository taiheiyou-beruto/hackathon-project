import numpy as np
# ツイートのDataFrameを引数とする．

# 文字列に「です」「ます」がいくつ含まれるかを返す
def countDesuMasu(str):
    desu_count = str.count("です")
    masu_count = str.count("ます")
    print(str)
    return desu_count + masu_count

def normalize(x, min_x, max_x):
    return (x - min_x) / (max_x - min_x)

def calculateEvaluationValue(df):
    # 各特徴量の上限値の定義
    max_favorite_count = 200
    max_ff_rate = 500.0
    max_listed_count = 1100
    max_retweet_count = 1000

    # フォロワー数とフォロー数の比
    df["ff_rate"] = df["followers_count"] / df["friends_count"]
    # プロフィールの文字数
    df["description_word_count"] = df["description"].apply(lambda x : len(x))
    # ツイート本文の文字数
    df["text_word_count"] = df["text"].apply(lambda x : len(x))
    # プロフィールの「です」「ます」の数
    df["description_DesuMasu_count"] = df["description"].apply(lambda x : countDesuMasu(x))

    # 正規化（上限値あり）
    df.favorite_count /= max_favorite_count
    df.favorite_count = df.favorite_count.where(df.favorite_count < 1, 1)
    df.ff_rate /= max_ff_rate
    df.ff_rate = df.ff_rate.where(df.ff_rate < 1, 1)
    df.listed_count /= max_listed_count
    df.listed_count = df.listed_count.where(df.listed_count < 1, 1)
    df.retweet_count /= max_retweet_count
    df.retweet_count = df.retweet_count.where(df.retweet_count < 1, 1)

    # 正規化（上限値なし）
    df["text_word_count_normalized"] = df["text_word_count"].apply(lambda x : normalize(x, df["text_word_count"].max(), df["text_word_count"].min()))

    # 評価値 まだ検討中
    df["point"] = 7*df["favorite_count"] + 5*df["ff_rate"] + 4.5*df["listed_count"] + 3.5*df["retweet_count"] + df["verified"]