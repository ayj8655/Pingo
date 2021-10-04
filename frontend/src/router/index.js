import { createRouter, createWebHistory } from 'vue-router'

import login from '../views/login.vue'
import lobby from '../views/lobby.vue'
import room from '../views/room.vue'

const routes = [

  {
    path: '/',
    name: 'login',
    component: login
  },
  {
    path: '/lobby',
    name: 'lobby',
    component: lobby
  },
  {
    path: '/room/:room_id',
    name: 'room',
    component: room
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
