<template>
  <header>
    <div class="menu" ref="menuBox">
      <div class="brand">
        <router-link to='/' class-active="active">
          Bayonet
        </router-link>
      </div>
      <div class="menu-toggle">
        <button
          class="hamburger hamburger--elastic open-menu"
          type="button"
          v-bind:class="[ isOpen ? 'is-active' : '']"
          v-on:click="toggleMenu"
          aria-label="Menu"
          aria-controls="navigation"
          aria-expanded="true/false">
          <span class="hamburger-box">
            <span class="hamburger-inner"></span>
          </span>
        </button>
      </div>
    </div>

    <nav class="navigation" v-bind:class="[ isOpen ? 'open' : '']" v-bind:style="menuStyles">
      <div class="wrapper">
        <router-link to='/total-transacciones' class-active="active">
          <span>
            Total por tipo de transacciones
          </span>
          <span class="desc">
            Muestra el total de cada tipo de transacción realizada
          </span>
        </router-link>
        <router-link to='/frecuencia-correos' class-active="active">
          <span>
            Frecuencia de correos
          </span>
          <span class="desc">
            Muestra la frecuencia de los dominios de los correos por cada tipo de transacción
          </span>
        </router-link>
        <router-link to='/frecuencia-nombres' class-active="active">
          <span>
            Frecuencia de nombres
          </span>
          <span class="desc">
            Muestra la frecuencia de los nombres y apellidos por cada tipo de transacción
          </span>
        </router-link>
        <router-link to='/frecuencia-tarjetas' class-active="active">
          <span>
            Frecuencia de tarjetas
          </span>
          <span class="desc">
            Muestra la frecuencia de card_bin y card_last_4 por cada tipo de transacción
          </span>
        </router-link>
        <router-link to='/monto-promedio' class-active="active">
          <span>
            Monto promedio por tipo de transacción
          </span>
          <span class="desc">
            Muestra el monto promedio por cada tipo de transacción
          </span>
        </router-link>
      </div>
    </nav>
  </header>
</template>

<script>
import Vue from 'vue';

import './styles.sass';

export default {
  name: 'app-header',
  data() {
    return {
      isOpen: false,
      menuStyles: {},
    };
  },
  mounted () {
    this.matchHeight();
  },
  watch: {
    '$route' () {
      if (this.isOpen) {
        this.toggleMenu();
      }
    }
  },
  methods: {
    toggleMenu() {
      this.isOpen = !this.isOpen;
    },
    matchHeight () {
      const height = this.$refs.menuBox.clientHeight;
      Vue.set(this.menuStyles, 'top', `${height}px`);
    }
  }
}
</script>
