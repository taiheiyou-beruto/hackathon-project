<template>
  <div class="body">
    <h1 class="text-center covid-title">都道府県累計感染者数</h1>
    <div class="graph rounded-lg">
      <bar :chart-data="graphData"></bar>
    </div>
  </div>
</template>



<script>

import axios from 'axios'
import Bar from '../../bar.js'

export default {
  components: {
    Bar
  },

//API格納用のプロパティ 都道府県累計感染者数
  data: function(){
    return{
      acp: [],
    }
  },

//axiosによるデータ取得処理
  mounted: function(){
    let _this=this
    console.log(this.acp)
    axios.get('https://data.corona.go.jp/converted-json/covid19japan-all.json')
    .then(function(response){
      //デバッグ用にconsoleに出力
      console.log(response.data[0].area)
      _this.acp = response.data[0].area
    })
    .catch(function(error){
      console.log(error)
    })
  },
  computed: {
    graphData() {
      const labels = this.acp.map(x => x.name_jp);
      console.log(labels);
      const nps = this.acp.map(y =>y.npatients)
      return ({
        labels,
        datasets: [{
          label: '都道府県累計感染者数',
          data: nps,
          borderWidth: 3,
          barPercentage: 1,
          backgroundColor: 'rgba(243, 87, 81, 0.8)',
          borderColor: 'rgba(243, 87, 81, 0.8)',
        }]
      })
    }
  }
}
</script>

<style scoped>
.body {
  height: 20vh;
  padding-top: 10rem;
}

.covid-title{
  margin-bottom: 1.2rem;
}

.graph{
  background-color: #2c3b4d;
  margin: 2px;
}
</style>