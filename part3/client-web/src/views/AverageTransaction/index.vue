<template>
  <div class="average-view">
    Promedio por tipo de transacción
    <pulse-loader color="#FF9F1C" size="20px"></pulse-loader>
  </div>
</template>

<script>
import Vue from 'vue';
import { PulseLoader } from 'vue-spinner/dist/vue-spinner.min.js';

export default {
  name: 'average-view',
  components: {
    PulseLoader,
  },
  mounted() {
    Vue.axios.get(this.$route.path).then((response) => {
      console.log(response.data)
    })
  }
}
</script>
