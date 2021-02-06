<template>
  <div class="body">
    <div class="form-block">
      <form action="" method="post" name="Form1">
      <div class="form-group">
        <label>お名前</label>
        <input type="text" class="form-control" placeholder="フォーム太朗" name="name" required>
        <span class="glyphicon form-control-feedback" aria-hidden="true"></span>
        <div class="help-block with-errors"></div>
      </div>
      <div class="form-group">
        <label>メールアドレス</label>
        <input type="email" class="form-control" placeholder="xxxxxx@xxxxxx" name="email" required>
        <span class="glyphicon form-control-feedback" aria-hidden="true"></span>
        <div class="help-block with-errors"></div>
      </div>
      <label>件名</label><br>
      <div class="form-group" style="margin-top:10px;">
        <input type="text" class="form-control" placeholder="〇〇について" name="subject" onClick="changeDisabled()">
      </div>
      <div class="form-group">
        <label>お問い合わせ内容</label>
        <textarea placeholder="お問い合わせ内容" rows="10" class="form-control" name="main" required></textarea>
        <span class="glyphicon form-control-feedback" aria-hidden="true"></span>
        <div class="help-block with-errors"></div>
      </div>
      <button type="submit" class="btn btn-lg btn-block btn-primary">送信</button>
    </form>
    </div>
  </div>
</template>

<script>
</script>

<style scoped>
.body{
  background: #afafaf;
  height: 100vh;
  padding-top: 10rem;
}

.form-block{
  width: 80%;
  margin: 0 auto;
}

.btn{
  margin-top: 3rem;
}

@media screen and (max-width: 575px){
  .body{
    padding-top: 6rem;
  }
}
</style>