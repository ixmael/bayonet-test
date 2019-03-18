<template>
  <div id="bayonet">
    <Header />
    <div class="container">
      <router-view />
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import Header from '@components/Header';

export default {
  name: 'app',
  components: {
    Header,
  },
  mounted() {
    if (!localStorage.filter) {
      Vue.axios.get('/metadata').then((response) => {
        const filter = {
          min: new Date(response.data.min),
          max: new Date(response.data.max),
          years: [],
        };

        const minYear = filter.min.getFullYear();
        const maxYear = filter.max.getFullYear();

        for (let i = minYear; i <= maxYear; i++) {
          filter.years.push({
            text: i,
            value: i,
          });
        }

        localStorage.filter = JSON.stringify(filter);
      });
    }
  },
}
</script>
