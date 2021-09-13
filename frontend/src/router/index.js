import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import main from '../views/main.vue'
import makeRoom from '../components/makeRoom.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/main',
    name: 'main',
    component: main
  },
  {
    path: '/makeRoom',
    name: 'makeRoom',
    component: makeRoom
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
