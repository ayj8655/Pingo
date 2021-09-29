import { createRouter, createWebHistory } from 'vue-router'

import login from '../views/login.vue'
import makeRoom from '../components/lobby/makeRoom.vue'
import lobby from '../views/lobby.vue'
import draw from '../components/room/draw.vue'
import room from '../views/room.vue'
import play from '../components/room/play.vue'
import score from '../components/room/score.vue'

const routes = [

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
