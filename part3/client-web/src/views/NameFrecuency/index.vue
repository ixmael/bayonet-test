<template>
  <div class="names-frecuency-view">
    <h1>
      Frecuencia de nombres
    </h1>
    <DataFilter @filter="handleFilter" />
    <div v-if="downloaded">
      <div v-if="transactions.length > 0">
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
import { PulseLoader } from 'vue-spinner/dist/vue-spinner.min.js';
import ViewMixin from '@mixins/ViewMixin';
import DataFilter from '@components/DataFilter';

import './styles.sass';

export default {
  name: 'names-frecuency-view',
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
        });

        this.downloaded = true;
        this.downloading = false;
      });
    },
  },
}
</script>
