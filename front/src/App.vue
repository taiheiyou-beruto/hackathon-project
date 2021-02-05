<template>
  <div class="body">
    <header>
      <nav class="navbar navbar-expand-sm fixed-top navbar-dark bg-dark">
        <div class="title-block" style="margin: 0 2rem;">
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

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300&display=swap');

.team-icon{
  margin-right: 2rem;
}

.menu-list{
  margin: 0 10px;
}

.body {
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
</style>
