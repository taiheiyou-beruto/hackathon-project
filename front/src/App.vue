<template>
  <div class="body">
    <header>
      <nav class="navbar navbar-expand-sm fixed-top navbar-dark bg-dark">
        <div class="title-block" style="margin-left: 2rem;">
          <a class="navbar-brand" href="#" style="font-size: 3rem;">CIiT</a>
        </div>
        <div class="collapse navbar-collapse" id="navbarNav" style="font-size: 1.3rem;">
          <ul class="navbar-nav">
            <li class="nav-item menu-list">
              <router-link to="/" class="nav-link">Home</router-link>
            </li>
            <li class="nav-item menu-list">
              <router-link to="/twitter" class="nav-link">Twitter</router-link>
            </li>
            <li class="nav-item menu-list">
              <router-link to="/informations" class="nav-link">COVID-19 informations</router-link>
            </li>
            <li class="nav-item menu-list">
              <router-link to="/contact" class="nav-link">Contact</router-link>
            </li>
          </ul>
        </div>


        <div class="pos-f-t smart-menu" style="width: 100%;">
          <div class="collapse" id="navbarToggleExternalContent">
          <div class="bg-dark p-4">
            <router-link to="/" class="nav-link">Home</router-link>
            <router-link to="/twitter" class="nav-link">Twitter</router-link>
            <router-link to="/informations" class="nav-link">COVID-19 informations</router-link>
            <router-link to="/contact" class="nav-link">Contact</router-link>
          </div>
          </div>
          <button class="navbar-toggler menu-btn" type="button" data-toggle="collapse" data-target="#navbarToggleExternalContent" aria-controls="navbarToggleExternalContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
        </div>

        <div class="team-icon">
          <img src="./img/team-icon.png" alt="" width="90">
        </div>
      </nav>
    </header>

    <div class="main">
      <router-view />
    </div>
  </div>
</template>

<script>
// import db from './firebase/firestore.js'
// export default {
//   mounted: function() {
//     // firestoreからデータを取ってくる処理
//     db.collection('#コロナ').get().then(res => {
//       res.forEach(doc => {
//         const data = doc.data()
//         console.log(data)
//       });
//     })
//   }
// }
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300&display=swap');

.title-block{
  margin-left: 2rem;
}

.team-icon{
  margin-right: 2rem;
}

.menu-list{
  margin: 0 10px;
  font-size: calc(8px + 1.2vw);
}

.menu-btn{
  margin-right: 0;
}

.smart-menu{
  display: none;
}

.body {
  height: 100vh;
  background: #afafaf;
  font-family: 'Noto Sans JP', sans-serif;
}

.card-deck{
  margin-top: 2rem;
}

.card-image{
  margin: 0.5rem;
}

.card-view-button{
  margin-top: 2rem;
}

@media screen and (max-width: 735px){
  .team-icon{
    display: none;
  }
}

@media screen and (max-width: 575px){
  .title-block{
    display: none;
  }

  .smart-menu{
    display: block;
  }

  .nav-link{
    text-decoration: none;
    color: rgb(255, 255, 255);
    font-size: 1.2rem;
  }
}
</style>
