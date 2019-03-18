import Vue from 'vue';
import axios from 'axios';
import VueGoogleCharts from 'vue-google-charts';
import VueAxios from 'vue-axios';

import App from '@components/App';
import router from './router';

import '@themes';

Vue.use(VueAxios, axios);
Vue.use(VueGoogleCharts);

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
