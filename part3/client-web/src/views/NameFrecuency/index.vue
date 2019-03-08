<template>
  <div class="names-frecuency-view">
    <h1>
      Frecuencia de nombres
    </h1>
    <div v-if="downloaded">
      <table>
        <thead>
          <tr>
            <th>
              Rank
            </th>
            <th colspan="2">
              Success
            </th>
            <th colspan="2">
              Suspected_fraud
            </th>
            <th colspan="2">
              Bank_decline
            </th>
            <th colspan="2">
              Chargeback
            </th>
          </tr>
          <tr>
            <th>
              &nbsp;
            </th>
            <th>
              Nombres
            </th>
            <th>
              Apellidos
            </th>
            <th>
              Nombres
            </th>
            <th>
              Apellidos
            </th>
            <th>
              Nombres
            </th>
            <th>
              Apellidos
            </th>
            <th>
              Nombres
            </th>
            <th>
              Apellidos
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(name, i) in transactions" :key="`name-${i}`" :class="getRowClass(i + 1)">
            <td class="rank">
              {{i+1}}
            </td>

            <td>
              <div class="name">
                <span>
                  {{name.success_name}}
                </span>
                <span class="frec">
                  {{name.success_name_frec}}
                </span>
              </div>
            </td>
            <td>
              <div class="lastname">
                <span>
                  {{name.success_lastname}}
                </span>
                <span class="frec">
                  {{name.success_lastname_frec}}
                </span>
              </div>
            </td>

            <td>
              <div class="name">
                <span>
                  {{name.suspected_fraud_name}}
                </span>
                <span class="frec">
                  {{name.suspected_fraud_name_frec}}
                </span>
              </div>
            </td>
            <td>
              <div class="lastname">
                <span>
                  {{name.suspected_fraud_lastname}}
                </span>
                <span class="frec">
                  {{name.suspected_fraud_lastname_frec}}
                </span>
              </div>
            </td>

            <td>
              <div class="name">
                <span>
                  {{name.bank_decline_name}}
                </span>
                <span class="frec">
                  {{name.bank_decline_name_frec}}
                </span>
              </div>
            </td>
            <td>
              <div class="lastname">
                <span>
                  {{name.bank_decline_lastname}}
                </span>
                <span class="frec">
                  {{name.bank_decline_lastname_frec}}
                </span>
              </div>
            </td>
            
            <td>
              <div class="name">
                <span>
                  {{name.chargeback_name}}
                </span>
                <span class="frec">
                  {{name.chargeback_name_frec}}
                </span>
              </div>
            </td>
            <td>
              <div class="lastname">
                <span>
                  {{name.chargeback_lastname}}
                </span>
                <span class="frec">
                  {{name.chargeback_lastname_frec}}
                </span>
              </div>
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

import './styles.sass';

export default {
  name: 'names-frecuency-view',
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
      Object.keys(response.data).forEach(transaction => {

        response.data[transaction]['names'].forEach((name, i) => {
          if (this.transactions.length <= i) {
            this.transactions.push({
              [`${transaction}_name`]: name[0],
              [`${transaction}_name_frec`]: name[1],
            });
          }
          else {
            this.transactions[i] = Object.assign({}, this.transactions[i], {
              [`${transaction}_name`]: name[0],
              [`${transaction}_name_frec`]: name[1],
            });
          }
        });

        response.data[transaction]['lastnames'].forEach((lastname, i) => {
          if (this.transactions.length <= i) {
            this.transactions.push({
              [`${transaction}_lastname`]: lastname[0],
              [`${transaction}_lastname_frec`]: lastname[1],
            });
          }
          else {
            this.transactions[i] = Object.assign({}, this.transactions[i], {
              [`${transaction}_lastname`]: lastname[0],
              [`${transaction}_lastname_frec`]: lastname[1],
            });
          }
        });
        this.downloaded = true;
      });
    })
  },
}
</script>
