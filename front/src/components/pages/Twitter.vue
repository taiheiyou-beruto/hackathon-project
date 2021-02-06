<template>
  <div class="body">
    <div class="main">
      <div class="container">
        <div class="row">
          <div class="col-xs-12 col-sm-12 col-md-6 col-lg-4 card-block" v-for='item in datalists' :key="item.id">
            <div class="card bg-dark text-light rounded-lg h-100" style="width: 100%;">
              <div class="text-center card-image">
                <img :src="item.profile_banner_url" class="card-img-top rounded-lg img-fluid" alt="Profile Image">
              </div>
              <div class="card-body">
                <p class="card-point">正確度偏差値: <span class="point">{{ item.point }}</span></p>
                <h5 class="card-title">{{ item.username }}</h5>
                <p class="card-text">{{ item.text }}</p>
                <div class="text-center card-view-button">
                  <button type="button" class="btn btn-primary terms-btn" data-toggle="modal" data-target="#exampleModalCenter" v-on:click="twitterInformation(item.id)">
                    More About
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalCenterTitle">ツイート</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body modal-text" v-if="!!twitterDetail">
              <h5>{{ twitterDetail.username }}</h5>
              <hr align="center" class="border">
              <p>{{ twitterDetail.description }}</p>
              <hr align="center" class="border">
              <p>{{ twitterDetail.text }}</p>
              <div class="twitter-count">
                <p>いいね数: {{ twitterDetail.favorite_count }} </p>
                <p>フォロワー数: {{ twitterDetail.followers_count}} </p>
                <p>フォロー中: {{ twitterDetail.friends_count }} </p>
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">閉じる</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import db from '../../firebase/firestore.js';
// import Vue from 'vue';

export default {
  data: function() {
    return {
      datalists: [],
      selectUserId : null,
    };
  },
  methods: {
    twitterInformation: function(id){
      this.selectUserId = id
    }
  },
  computed: {
    twitterDetail: function(){
      const selectUserId = this.selectUserId;
      return this.datalists.find(doc => doc.id === selectUserId)
    }
  },
  mounted: async function() {

    // firestoreからデータを取ってくる処理
    const res = await db.collection("#コロナ").orderBy('point','desc').get()
    this.datalists = res.docs.map(doc => doc.data())
    console.log(this.datalists)
  }
}


</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300&display=swap');

.menu-list{
  margin: 0 10px;
}

.main{
  padding: 8rem 0;
  background: #afafaf;
}

.body {
  font-family: 'Noto Sans JP', sans-serif;
}

.card-block{
  margin-top: 2rem;
}

.card-image{
  margin: 0.5rem;
}

/* .card-img-top{
  height: 7rem;
} */

.card-point{
  color: rgb(224, 202, 4);
}

.point{
  font-size: calc(7px + 2vw);
}

.card-title{
  color: rgb(221, 125, 0);
}

.border{
  border: 1px solid #000000;
}

.card-view-button{
  margin-top: 2rem;
}

.modal{
  color: #000;
}

.twitter-count{
  display: flex;
  justify-content: space-around;
}

@media screen and (max-width: 767px){
  /* .card-img-top{
    height: 10rem;
  } */
}

@media screen and (max-width: 575px){
  .main{
    padding: 5rem 0;
  }

  .card-deck{
    width: auto;
  }

  /* .card-img-top{
    height: 7rem;
  } */
}
</style>
