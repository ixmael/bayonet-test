<template>
  <div class="total-transaction-view">
    <h1>
      Total de transacciones
    </h1>
    <div v-if="downloaded">
      <GChart
        type="ColumnChart"
        :data="transactions"
        :options="chartOptions"
      />
    </div>
    <div class="loading" v-else>
      <pulse-loader color="#FF9F1C" size="20px"></pulse-loader>
      <div class="loading-message">Esperando la carga de los datos</div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import { GChart } from 'vue-google-charts';
import { PulseLoader } from 'vue-spinner/dist/vue-spinner.min.js';

export default {
  name: 'total-transaction-view',
  data() {
    return {
      downloaded: false,
      transactions: [
        ['Tipo de transacción', 'Total de transacciones'],
      ],
      chartOptions: {
        chart: {
          title: 'Transacciones',
          subtitle: 'Sales, Expenses, and Profit: 2014-2017',
          hAxis: {
            title: 'Tipo de transacción'
          },
          vAxis: {
            title: 'Número de transacciones',
          },
        }
      }
    };
  },
  components: {
    PulseLoader,
    GChart,
  },
  mounted() {
    Vue.axios.get(this.$route.path).then((response) => {
      Object.keys(response.data).forEach(transaction_type => {
        this.transactions.push([transaction_type, response.data[transaction_type]]);
      });

      this.downloaded = true;
    })
  }
}
</script>
