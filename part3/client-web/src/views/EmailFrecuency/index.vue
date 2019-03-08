<template>
  <div class="email-frecuency-view">
    <h1>
      Frecuencia de correos
    </h1>
    <div v-if="downloaded">
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
  name: 'email-frecuency-view',
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
        this.downloaded = true;
      });
    })
  },
}
</script>
