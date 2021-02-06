<template>
  <div class="body">
    <div class="main-text-block">
      <h1 class="main-text-h1">CIiT(COVID-19 Informations in Twiter)へようこそ！</h1>
      <h2 class="main-text-h2">以下の利用規約を読んだ後にサイトを楽しみましょう</h2>
    </div>

    <div class="terms">

      <button type="button" class="btn btn-primary terms-btn" data-toggle="modal" data-target="#exampleModalCenter">
        利用規約
      </button>

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
              <p>・情報の表示の信頼性は上から順に高くなり、下にいくほど低くなっています</p>
              <p>・このサイトはプロトタイプとなっています。完成版ではありません</p>
              <p>・あらゆる情報に惑わされず、自分自身で取捨選択するようにしてください</p>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">同意しない</button>
              <button type="button" class="btn btn-primary" data-dismiss="modal">同意する</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <footer>
      <p>このWebサイトはチームA：太平洋ベルトが運営しています</p>
    </footer>
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

.main-text-block {
  width: 80%;
  margin: 0 auto;
}

.main-text-h1{
  font-size: calc(20px + 2vw);
  margin-bottom: 2rem;
}

.main-text-h2{
  font-size: calc(10px + 2vw);
}

.terms{
  text-align: center;
  margin-top: 4rem;
}

.terms-btn{
  padding: 20px 70px;
  font-size: 20px;
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