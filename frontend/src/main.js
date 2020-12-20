import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import "tailwindcss/tailwind.css";
import "./assets/app.css";
import "./assets/fonts/stylesheet.css";

import VueExcelXlsx from "vue-excel-xlsx";

Vue.use(VueExcelXlsx);
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
