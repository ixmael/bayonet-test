<template>
  <div class="average-view">
    <h1>
      Promedio por tipo de transacción
    </h1>
    <DataFilter @filter="handleFilter" />
    <div v-if="downloaded">
      <div v-if="transactions">
        <table>
          <thead>
            <tr>
              <th>
                Tipo de transacción
              </th>
              <th>
                Monto promedio de todas las transacciones
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(transaction, i) in transactions" :key="`transaction-${i}`" :class="getRowClass(i + 1)">
              <td>
                {{transaction.transaction}}
              </td>
              <td>
                {{transaction.amount}}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div v-else>
        No hay resultados
      </div>
    </div>
    <div class="loading" v-else-if="downloading">
      <pulse-loader color="#FF9F1C" size="20px"></pulse-loader>
      <div class="loading-message">Esperando la carga de los datos</div>
    </div>
    <div class="filtering" v-else>
      Preparar
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import { PulseLoader } from 'vue-spinner/dist/vue-spinner.min.js';
import ViewMixin from '@mixins/ViewMixin';
import DataFilter from '@components/DataFilter';

export default {
  name: 'average-view',
  mixins: [ViewMixin],
  data() {
    return {
      downloading: false,
      downloaded: false,
      transactions: [],
    };
  },
  components: {
    PulseLoader,
    DataFilter,
  },
  methods: {
    handleFilter(params) {
      this.downloading = true;
      this.downloaded = false;
      Vue.axios.get(this.$route.path, { params }).then((response) => {
        this.transactions = [];
        Object.keys(response.data).forEach(transaction_type => {
          this.transactions.push({
            transaction: transaction_type,
            amount: response.data[transaction_type],
          });
        });
        this.downloaded = true;
        this.downloading = false;
      })
    },
  },
}
</script>
