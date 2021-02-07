<template>
  <div class="body">
    <div class="center-border">
      <div class="container">
        <div class="row">
          <div class="main-text-block col-lg-12 col-xs-12">
            <h1 class="main-text-h1">CIiT(COVID-19 Informations in Twitter)へようこそ！</h1>
          </div>
        </div>
      </div>

      <div class="terms">
        <div class="container">
          <div class="row">
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-4 offset-md-3 offset-lg-4">
              <button type="button" class="btn btn-primary terms-btn" data-toggle="modal" data-target="#exampleModalCenter">
                利用規約
              </button>
            </div>
          </div>
        </div>

        <div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalCenterTitle">利用規約</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div class="modal-body modal-text">
                <p>・ここでの情報の信頼性はあくまでも運営側の主観が入っているため、その情報によって不利益が生じても運営は一切の責任を取りません。あくまでも参考程度にしてください</p>
                <p>・ツイートはコロナ関連だけのものとし、運営側が独断で選んだものとなっています</p>
                <p>・ツイートはTwitter APIから取得しており、改ざん等は一切行っておりません</p>
                <p>・このサイトを運営する上で以下URLのTwitter社の開発者利用規約を遵守しています</p>
                <p><a href="https://developer.twitter.com/en/developer-terms/agreement-and-policy">https://developer.twitter.com/en/developer-terms/agreement-and-policy</a></p>
                <p>・Twitter APIで取ってきたデータは評価値の計算以外の目的に使用いたしません</p>
                <p>・情報の表示の信頼性は上から順に高くなり、下にいくほど低くなっています</p>
                <p>・このサイトはプロトタイプとなっています。完成版ではありません</p>
                <p>・あらゆる情報に惑わされず、自分自身で取捨選択するようにしてください</p>
                <hr align="center" class="border">
                <p>このサイトはチームA:太平洋ベルトが運営しています</p>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">同意しない</button>
                <button type="button" class="btn btn-primary" data-dismiss="modal">同意する</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {

}

</script>

<style scoped>
.body{
  height: 100vh;
  padding-top: 10rem;
}

.center-border{
  display: table;
  width: 100%;
  height: 20rem;
  background-color: #e8a337;
  margin-top: 5rem;
}

.main-text-block {
  margin-top: 2rem;
}

.main-text-h1{
  font-size: calc(20px + 2vw);
  margin-bottom: 2rem;
  color: #fff;
}

.main-text-h2{
  font-size: calc(10px + 2vw);
}

.terms{
  text-align: center;
  margin-top: 4rem;
}

.terms-btn{
  width: 100%;
  padding: 10px 0;
  margin-bottom: 20px;
  font-size: calc(10px + 1.1vw);
}

.modal-text{
  text-align-last: left;
}

footer{
  width: 80%;
  margin: 0 auto;
  font-size: calc(10px + 1.2vw);
  margin-top: 4rem;
}

@media screen and (max-width: 575px){
  .body{
    padding-top: 6rem;
  }
}
</style>