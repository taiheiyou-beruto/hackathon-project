### back
APIキー直書きスタイルなので，Githubにはキー無しをアップしています．<br>
それに合わせて，キー無しを区別するため最後に_copyをつけています．<br>

- BackendMain.py<br>
メインクラス
  * Tweetの取得
  * evaluationFunctionの呼び出し
  * 必要データのFirestoreに書き込み

- evaluationFunction<br>
サブクラス
  * Tweetを分析し評価値を付与
  * Pandas.DataFrame型に成型して変数を保持
