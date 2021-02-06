<template>
  <div class="body">
    <h1>Informations</h1>
    <div class="text-center card-image">
                <img :src="item.profile_banner_url" class="card-img-top rounded-lg" alt="Profile Image">
              </div>
              <div class="card-body">
                <h5 class="card-title">{{ item.username }}</h5>
                <p class="card-text">{{ item.text }}</p>
                <div class="text-center card-view-button">
                  <a href="#" class="btn btn-primary">More about</a>
                </div>
              </div>
  </div>
</template>

<script >
export default {
}
</script>

<style scoped>
.body{
  height: 100vh;
  background: #afafaf;
  padding-top: 10rem;
}

@media screen and (max-width: 575px){
  .body{
    padding-top: 6rem;
  }
}
</style>