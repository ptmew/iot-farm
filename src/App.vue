<template>
  <div>
    <h1>{{Title}}</h1>
    <button>Dashboard</button>
    <button>Data History</button>
    <h2>Temprature: 20°</h2>
    <h2>Humidity: 55%</h2>
    <h2>Oxygen:150 Mg</h2>
    <h2>PH: 6.4</h2>
    <h2>EC: 3</h2>
    <h2>EC: 3</h2>
  <router-view></router-view>
  </div>
</template>

<script>
export default {
  name:"app",
  data() {
    return {
      Title:"Bally Smartfarm",
    }
  },

};
</script>

<style>

</style>




