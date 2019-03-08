<template>
  <div id="bayonet">
    <Header />
    <div class="container">
      <router-view />
    </div>
  </div>
</template>

<script>
import Header from '@components/Header';

export default {
  name: 'app',
  components: {
    Header,
  },
}
</script>
