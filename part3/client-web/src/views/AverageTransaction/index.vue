<template>
  <div class="average-view">
    <h1>
      Promedio por tipo de transacción
    </h1>
    <div v-if="downloaded">
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
    <div class="loading" v-else>
      <pulse-loader color="#FF9F1C" size="20px"></pulse-loader>
      <div class="loading-message">Esperando la carga de los datos</div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import { PulseLoader } from 'vue-spinner/dist/vue-spinner.min.js';
import ViewMixin from '@mixins/ViewMixin';

export default {
  name: 'average-view',
  mixins: [ViewMixin],
  data() {
    return {
      downloaded: false,
      transactions: [],
    };
  },
  components: {
    PulseLoader,
  },
  mounted() {
    Vue.axios.get(this.$route.path).then((response) => {
      Object.keys(response.data).forEach(transaction_type => {
        this.transactions.push({
          transaction: transaction_type,
          amount: response.data[transaction_type],
        });
      });

      this.downloaded = true;
    })
  }
}
</script>
