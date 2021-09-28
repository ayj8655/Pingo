import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import login from '../views/login.vue'
import makeRoom from '../components/makeRoom.vue'
import lobby from '../views/lobby.vue'
import draw from '../components/draw.vue'
import room from '../views/room.vue'
import play from '../views/play.vue'
import score from '../views/score.vue'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: login
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
    path: '/login',
    name: 'login',
    component: login
  },
  {
    path: '/makeRoom',
    name: 'makeRoom',
    component: makeRoom
  },
  {
    path: '/lobby',
    name: 'lobby',
    component: lobby
  },
  {
    path: '/draw',
    name: 'draw',
    component: draw
  },
  {
    path: '/room/:room_id',
    name: 'room',
    component: room
  },
  {
    path: '/play/:room_id',
    name: 'play',
    component: play
  },
  {
    path: '/play/score',
    name: 'score',
    component: score
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
