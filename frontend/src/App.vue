<template>
  <div class="container">
    <div class="row mt-5">
      <div class="col">
        <h1 class="text-center">BALLY SMART FARM</h1>
      </div>
    </div>
    <div class="row mt-5" v-if="arrPositive.length > 0">
      <div class="col">
        <h2 class="text-center">HUMIDITY</h2>
        <line-chart
          :chartData="arrPositive"
          :options="chartOptions"
          :chartColors="positiveChartColors"
          label="HUMID"
        />
      </div>
    </div>

    <div class="row mt-5" v-if="arrHospitalized.length > 0">
      <div class="col">
        <h2 class="text-center">TEMPERATURE</h2>
        <line-chart
          :chartData="arrHospitalized"
          :options="chartOptions"
          :chartColors="hospitalizedChartColors"
          label="TEMP"
        />
      </div>
    </div>

    <div class="row mt-5" v-if="arrInIcu.length > 0">
      <div class="col">
        <h2 class="text-center">POTENTIAL HYDROGEN</h2>
        <line-chart
          :chartData="arrInIcu"
          :options="chartOptions"
          :chartColors="inIcuColors"
          label="PH"
        />
      </div>
    </div>

    <div class="row mt-5" v-if="arrOnVentilators.length > 0">
      <div class="col">
        <h2 class="text-center">ELECTRICAL CONDUCTIVITY</h2>
        <line-chart
          :chartData="arrOnVentilators"
          :options="chartOptions"
          :chartColors="onVentilatorsColors"
          label="EC"
        />
      </div>
    </div>

    <div class="row mt-5" v-if="arrRecovered.length > 0">
      <div class="col">
        <h2 class="text-center">OXYGEN</h2>
        <line-chart
          :chartData="arrRecovered"
          :options="chartOptions"
          :chartColors="recoveredColors"
          label="O2"
        />
      </div>
    </div>

  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";

import LineChart from "./components/LineChart";

export default {
  components: {
    LineChart
  },
  data() {
    return {
      arrPositive: [],
      positiveChartColors: {
        borderColor: "#077187",
        pointBorderColor: "#0E1428",
        pointBackgroundColor: "#AFD6AC",
        backgroundColor: "#74A57F"
      },
      arrHospitalized: [],
      hospitalizedChartColors: {
        borderColor: "#251F47",
        pointBorderColor: "#260F26",
        pointBackgroundColor: "#858EAB",
        backgroundColor: "#858EAB"
      },
      arrInIcu: [],
      inIcuColors: {
        borderColor: "#190B28",
        pointBorderColor: "#190B28",
        pointBackgroundColor: "#E55381",
        backgroundColor: "#E55381"
      },
      arrOnVentilators: [],
      onVentilatorsColors: {
        borderColor: "#784F41",
        pointBorderColor: "#784F41",
        pointBackgroundColor: "#BBE5ED",
        backgroundColor: "#BBE5ED"
      },
      arrRecovered: [],
      recoveredColors: {
        borderColor: "#4E5E66",
        pointBorderColor: "#4E5E66",
        pointBackgroundColor: "#31E981",
        backgroundColor: "#31E981"
      },
      arrDeaths: [],
      deathColors: {
        borderColor: "#E06D06",
        pointBorderColor: "#E06D06",
        pointBackgroundColor: "#402A2C",
        backgroundColor: "#402A2C"
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false
      }
    };
  },
  async created() {
    const  data = await axios.get("https://aweokl79gc.execute-api.us-east-1.amazonaws.com/test/api?query=select * from PLANT_STATUS");
    data.data.forEach(d => {
      const date = moment(d.TIMESTAMP).format("MM/DD/YY HH:mm:ss");
      const {
        NAME,
        HUMID,
        TEMP,
        PH,
        EC,
        O2
      } = d;

      this.arrPositive.push({ date, total: HUMID });
      this.arrHospitalized.push({ date, total: TEMP });
      this.arrInIcu.push({ date, total: PH });
      this.arrOnVentilators.push({ date, total: EC });
      this.arrRecovered.push({ date, total: O2 });
      this.arrDeaths.push({ date, total: NAME });      
    });
    
  }
};
</script>

<style>
</style>
