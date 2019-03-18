<template>
  <div class="data-filter">
    <div class="month">
      <select v-model="monthSelected">
        <option value="1">Enero</option>
        <option value="2">Febrero</option>
        <option value="3">Marzo</option>
        <option value="4">Abril</option>
        <option value="5">Mayo</option>
        <option value="6">Junio</option>
        <option value="7">Julio</option>
        <option value="8">Agosto</option>
        <option value="9">Septiembre</option>
        <option value="10">Octubre</option>
        <option value="11">Noviembre</option>
        <option value="12">Diciembre</option>
      </select>
    </div>
    <div class="year">
      <select v-model="yearSelected">
        <option v-for="year in years" v-bind:key="year.value" v-bind:value="year.value">
          {{ year.text }}
        </option>
      </select>
    </div>
    <button class="button-flat filter-apply" title="Filtrar los resultados" v-on:click="initLoadData">
      <span v-if="monthSelected || yearSelected">
        Filtrar
      </span>
      <span v-else>
        Todo
      </span>
      <i class="fas fa-search"></i>
    </button>
    <button class="button-flat filter-clean" title="Eliminar el filtro" v-on:click="clearFilter">
      Limpiar <i class="fas fa-trash-alt"></i>
    </button>
  </div>
</template>

<script>
import { library, dom } from "@fortawesome/fontawesome-svg-core";
import { faTrashAlt } from "@fortawesome/free-solid-svg-icons/faTrashAlt";
import { faSearch } from "@fortawesome/free-solid-svg-icons/faSearch";

import './styles.sass';

library.add(faTrashAlt);
library.add(faSearch);
dom.watch();

export default {
  name: 'data-filter',
  props: [ 'loadData' ],
  data() {
    const filter = JSON.parse(localStorage.getItem('filter'));
    return {
      hasFiltered: false,
      min: new Date(filter.min),
      max: new Date(filter.max),
      years: filter.years,
      monthSelected: null,
      yearSelected: null,
    };
  },
  methods: {
    clearFilter() {
      this.monthSelected = null;
      this.yearSelected = null;
    },
    initLoadData() {
      this.$emit('filter', {
        month: this.monthSelected,
        year: this.yearSelected,
      });
    },
  },
}
</script>
