<template>
  <div class="card-frecuency-view">
    <h1>
      Frecuencia de tarjetas
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
              Card bin
            </th>
            <th>
              Card last 4
            </th>
            <th>
              Card bin
            </th>
            <th>
              Card last 4
            </th>
            <th>
              Card bin
            </th>
            <th>
              Card last 4
            </th>
            <th>
              Card bin
            </th>
            <th>
              Card last 4
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(card, i) in transactions" :key="`name-${i}`" :class="getRowClass(i + 1)">
            <td class="rank">
              {{i+1}}
            </td>

            <td>
              <div class="card_bin">
                <span>
                  {{card.success_card_bin}}
                </span>
                <span class="frec">
                  {{card.success_card_bin_frec}}
                </span>
              </div>
            </td>
            <td>
              <div class="card_last_4">
                <span>
                  {{card.success_card_last_4}}
                </span>
                <span class="frec">
                  {{card.success_card_last_4_frec}}
                </span>
              </div>
            </td>

            <td>
              <div class="card_bin">
                <span>
                  {{card.suspected_fraud_card_bin}}
                </span>
                <span class="frec">
                  {{card.suspected_fraud_card_bin_frec}}
                </span>
              </div>
            </td>
            <td>
              <div class="card_last_4">
                <span>
                  {{card.suspected_fraud_card_last_4}}
                </span>
                <span class="frec">
                  {{card.suspected_fraud_card_last_4_frec}}
                </span>
              </div>
            </td>

            <td>
              <div class="card_bin">
                <span>
                  {{card.bank_decline_card_bin}}
                </span>
                <span class="frec">
                  {{card.bank_decline_card_bin_frec}}
                </span>
              </div>
            </td>
            <td>
              <div class="card_last_4">
                <span>
                  {{card.bank_decline_card_last_4}}
                </span>
                <span class="frec">
                  {{card.bank_decline_card_last_4_frec}}
                </span>
              </div>
            </td>
            
            <td>
              <div class="card_bin">
                <span>
                  {{card.chargeback_card_bin}}
                </span>
                <span class="frec">
                  {{card.chargeback_card_bin_frec}}
                </span>
              </div>
            </td>
            <td>
              <div class="card_last_4">
                <span>
                  {{card.chargeback_card_last_4}}
                </span>
                <span class="frec">
                  {{card.chargeback_card_last_4_frec}}
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
  name: 'card-frecuency-view',
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
        response.data[transaction]['card_bin'].forEach((cards, i) => {
          if (this.transactions.length < i) {
            this.transactions.push({
              [`${transaction}_card_bin`]: cards[0],
              [`${transaction}_card_bin_frec`]: cards[1],
            });
          }
          else {
            this.transactions[i] = Object.assign({}, this.transactions[i], {
              [`${transaction}_card_bin`]: cards[0],
              [`${transaction}_card_bin_frec`]: cards[1],
            });
          }
        });

        response.data[transaction]['card_last_4'].forEach((cards, i) => {
          if (this.transactions.length < i) {
            this.transactions.push({
              [`${transaction}_card_last_4`]: cards[0],
              [`${transaction}_card_last_4_frec`]: cards[1],
            });
          }
          else {
            this.transactions[i] = Object.assign({}, this.transactions[i], {
              [`${transaction}_card_last_4`]: cards[0],
              [`${transaction}_card_last_4_frec`]: cards[1],
            });
          }
        });
      });
      this.downloaded = true;
    })
  },
}
</script>
