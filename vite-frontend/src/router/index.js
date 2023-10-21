import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory("/"),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: "/wheel/:id",
      name: "wheel",
      component: () => import("../views/WheelDetail.vue"),
      props: true
    },
    {
      path: "/order/:id",
      name: "order",
      component: () => import("../views/OrderWheel.vue"),
      props: true
    },
    {
      path: "/search",
      name: "search",
      component: () => import("../views/SearchWheel.vue"),
      props: true
    },
  ]
})

export default router
