<template>
  <div class="email-frecuency-view">
    <h1>
      Frecuencia de correos
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
              <th>
                Success
              </th>
              <th>
                Suspected_fraud
              </th>
              <th>
                Bank_decline
              </th>
              <th>
                Chargeback
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(email, i) in transactions" :key="`email-${i}`" :class="getRowClass(i + 1)">
              <td class="rank">
                {{i+1}}
              </td>
              <td>
                <div class="email">
                  <span>
                    {{email.success_email}}
                  </span>
                  <span class="frec">
                    {{email.success_frec}}
                  </span>
                </div>
              </td>
              <td>
                <div class="email">
                  <span>
                    {{email.suspected_fraud_email}}
                  </span>
                  <span class="frec">
                    {{email.suspected_fraud_frec}}
                  </span>
                </div>
              </td>
              <td>
                <div class="email">
                  <span>
                    {{email.bank_decline_email}}
                  </span>
                  <span class="frec">
                    {{email.bank_decline_frec}}
                  </span>
                </div>
              </td>
              <td>
                <div class="email">
                  <span>
                    {{email.chargeback_email}}
                  </span>
                  <span class="frec">
                    {{email.chargeback_frec}}
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
  name: 'email-frecuency-view',
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
          response.data[transaction].forEach((email, i) => {
            if (this.transactions.length <= i) {
              this.transactions.push({
                [`${transaction}_email`]: email[0],
                [`${transaction}_frec`]: email[1],
              });
            }
            else {
              this.transactions[i] = Object.assign({}, this.transactions[i], {
                [`${transaction}_email`]: email[0],
                [`${transaction}_frec`]: email[1],
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
