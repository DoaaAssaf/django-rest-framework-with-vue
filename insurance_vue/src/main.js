// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import vueResource from "vue-resource"
import VueRouter from "vue-router"
import index from "./components/index"
import addCarRisk from "./components/addCarRisk"
import viewRisks from "./components/view.vue"
import Dropdown from "hsy-vue-dropdown"
import VueAgile from 'vue-agile'


Vue.config.productionTip = false

Vue.use(VueAgile)
Vue.use(Dropdown)
Vue.use(vueResource)
Vue.use(VueRouter)

const router = new VueRouter({
  mode: "history",
  base: __dirname,
  routes:[
    {path:"/index",component:index},
    {path:"/viewRisks", component:viewRisks},
    {path:"/addCarRisk", component:addCarRisk}

  ]
});


new Vue({
  el: '#app',
 template: '<App/>',
 components: { App },
  router,
}).$mount("#app")

