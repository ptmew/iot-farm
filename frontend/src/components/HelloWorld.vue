<template>
<div>
  <chartjs-doughnut v-bind:labels="labels"
    v-bind:datasets="datasets"
    v-bind:option="option"></chartjs-doughnut>
</div>
</template>

<script>
export default {
  data() {
    return {
      labels:["good","bad"],
      datasets: [
        {
          data: [50,50],
          backgroundColor: ["Green", "Red"]
        }
      ],
      option:{
        title: {
          display: true,
          position: "bottom",
          text: "Temperature"
        }
      }
    };
  }
};
</script>

<style scoped>

</style>