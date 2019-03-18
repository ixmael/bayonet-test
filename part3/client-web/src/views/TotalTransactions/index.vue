<template>
  <div class="total-transaction-view">
    <h1>
      Total de transacciones
    </h1>
    <DataFilter @filter="handleFilter" />
    <div v-if="downloaded">
      <div v-if="transactions.length > 1">
        <GChart
          type="ColumnChart"
          :data="transactions"
          :options="chartOptions"
        />
      </div>
      <div class="filtering" v-else>
        No hay resultados
      </div>
    </div>
    <div class="loading" v-else-if="downloading">
      <pulse-loader color="#FF9F1C" size="20px"></pulse-loader>
      <div class="loading-message">Esperando la carga de los datos</div>
    </div>
    <div class="filtering" v-else>
      No se ha solicitado ningún dato.
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import { GChart } from 'vue-google-charts';
import { PulseLoader } from 'vue-spinner/dist/vue-spinner.min.js';
import DataFilter from '@components/DataFilter';

import './styles.sass';

export default {
  name: 'total-transaction-view',
  data() {
    return {
      downloading: false,
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
    DataFilter,
  },
  methods: {
    handleFilter(params) {
      this.downloading = true;
      this.downloaded = false;

      Vue.axios.get(this.$route.path, { params }).then((response) => {
        this.transactions = [['Tipo de transacción', 'Total de transacciones']];

        Object.keys(response.data).forEach(transaction_type => {
          this.transactions.push([transaction_type, response.data[transaction_type]]);
        });

        this.downloaded = true;
        this.downloading = false;
      });
    },
  },
}
</script>
