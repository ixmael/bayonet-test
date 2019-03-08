<template>
  <div class="total-transaction-view">
    <h1>
      Total de transacciones
    </h1>
    <div v-bind:id="containerId" v-if="downloaded">
      Cargado
    </div>
    <div class="loading" v-else>
      <pulse-loader color="#FF9F1C" size="20px"></pulse-loader>
      <div class="loading-message">Esperando la carga de los datos</div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import { PulseLoader } from 'vue-spinner/dist/vue-spinner.min.js';

export default {
  name: 'total-transaction-view',
  data() {
    return {
      downloaded: false,
    };
  },
  components: {
    PulseLoader,
  },
  mounted() {
    Vue.axios.get(this.$route.path).then((response) => {
      this.downloaded = true;
      console.log(response.data);
    })
  }
}
</script>
