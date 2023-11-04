<template>
  <div>
    <apexchart
      :options="chartOptions"
      :series="series"
      type="radar"
      height="350"
      width="350"
    />
  </div>
</template>

<script>
import VueApexCharts from "vue-apexcharts";

export default {
  components: {
    apexchart: VueApexCharts,
  },
  props: {
    seriesData: {
      type: Array,
      default: () => [],
    },
    xaxisCategories: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      series: [
        {
          name: "Value",
          data: this.seriesData,
        },
      ],
      chartOptions: {
        chart: {
          type: "radar",
          toolbar: {
            show: false,
          },
        },
        xaxis: {
          categories: this.xaxisCategories,
        },
      },
    };
  },
};
</script>
