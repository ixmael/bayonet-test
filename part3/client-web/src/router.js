import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);



'/'
'/'
'/'
'/'

const router = new Router({
  // mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/total-transacciones',
      name: 'total-transactions',
      component: () => import(/* webpackChunkName: "page-total-transactions" */ '@views/TotalTransactions'),
    },
    {
      path: '/frecuencia-correos',
      name: 'email-frecuency',
      component: () => import(/* webpackChunkName: "page-email-frecuency" */ '@views/EmailFrecuency'),
    },
    {
      path: '/frecuencia-nombres',
      name: 'name-frecuency',
      component: () => import(/* webpackChunkName: "page-name-frecuency" */ '@views/NameFrecuency'),
    },
    {
      path: '/frecuencia-tarjetas',
      name: 'card-frecuency',
      component: () => import(/* webpackChunkName: "page-card-frecuency" */ '@views/CardFrecuency'),
    },
    {
      path: '/monto-promedio',
      name: 'avg-amount',
      component: () => import(/* webpackChunkName: "page-avg-amoint" */ '@views/AverageTransaction'),
    },
    {
      path: '/',
      name: 'home',
      component: () => import(/* webpackChunkName: "page-home" */ '@views/Home'),
    },
  ],
});

export default router;
