import Vue from "vue";
import Router from "vue-router";

import Index from "./components/pages/Index.vue";
import Twitter from "./components/pages/Twitter.vue";
import Informations from "./components/pages/Informations.vue";
import Contact from "./components/pages/Contact.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      component: Index
    },
    {
      path: '/twitter',
      component: Twitter
    },
    {
      path: '/informations',
      component: Informations
    },
    {
      path: '/contact',
      component: Contact
    }
  ]
});