
<template>
  <div>
  <div class="header">
    <a href="#"   class="title" style="font-size: 40px;">CIiT</a>  
     </div> 
  <div class="mx-auto main" style="width: 80%">
    <div class="card-deck" style="width:100%">
      <div class="card" style="width: 18rem;">
       <img src="./img/a.png" class="card-img-top" alt="...">
       <div class="card-body">
         <p class="card-text">twitterの情報の一部</p>
         <a href="#" class="btn btn-sm">詳細</a>
       </div>
      </div>

      <div class="card" style="width: 18rem;">
       <img src="./img/a.png" class="card-img-top" alt="...">
       <div class="card-body">
         <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
       </div>
      </div>  

      <div class="card" style="width: 18rem;">
       <img src="./img/a.png" class="card-img-top" alt="...">
       <div class="card-body">
         <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
       </div>
      </div>  
      </div> 

      <div class="card-deck" style="width:100%">
      <div class="card" style="width: 18rem;">
       <img src="./img/a.png" class="card-img-top" alt="...">
       <div class="card-body">
         <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
       </div>
      </div>

      <div class="card" style="width: 18rem;">
       <img src="./img/a.png" class="card-img-top" alt="...">
       <div class="card-body">
         <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
       </div>
      </div>  

      <div class="card" style="width: 18rem;">
       <img src="./img/a.png" class="card-img-top" alt="...">
       <div class="card-body">
         <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
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

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.card-deck {
  margin-top: 2rem;
  
  
}
body {
  background: linear-gradient(#05FBFF, #1E00FF);
}
.title {
    color: olive;
}
.header{
  text-align: center;
  height: 10%;
  background: black;
  position: fixed;
  width: 100%;
  top: 0;
  z-index: 1;
}
.main{
  margin-top: 10%;

}
</style>
