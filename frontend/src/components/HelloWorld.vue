<template>
<div>
  <chartjs-line v-bind:beginzero="beginZero"
    v-bind:datalabel="datalabel" v-bind:labels="labels"
    v-bind:data="data" v-bind:fill="fill"
    v-bind:bodercolor="boderColor"/>
</div>
</template>

<script>
export default {
  data() {
    return {
      beginZero: true,
      datalabel: "Temperature",
      labels: [1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00, 11.00, 12.00, 13.00, 14.00, 15.00, 16.00, 17.00, 18.00, 19.00, 20.00, 21.00, 22.00, 23.00, 0.00],
      data: [19, 19, 18, 18, 19, 20, 20, 20, 21, 21, 25, 27, 28, 28, 28, 27, 26, 25, 24, 24, 24, 22, 21, 20],
      fill: true,
      bgColor: "pink",
      borderColor: "	#FF0000"
      
      
    }
  }
};
</script>

<style scoped>

</style>