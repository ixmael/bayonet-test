import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
 

import App from '@components/App';
import router from './router';

import '@themes';

Vue.use(VueAxios, axios);

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
