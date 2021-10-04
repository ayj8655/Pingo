import { createRouter, createWebHistory } from 'vue-router'

import login from '../views/login.vue'
import makeRoom from '../components/lobby/makeRoom.vue'
import lobby from '../views/lobby.vue'
import draw from '../components/room/draw.vue'
import room from '../views/room.vue'
import playRoom from '@/components/room/playRoom.vue'
import playReady from '@/components/room/playReady.vue'
import play from '../components/room/play.vue'
import score from '../components/room/score.vue'

const routes = [

  {
    path: '/',
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
    path: '/playRoom/:room_id',
    name: 'playRoom',
    component: playRoom,
    children: [
      {
        // /user/:id/profile 과 일치 할 때
        // UserProfile은 User의 <router-view> 내에 렌더링 됩니다.
        path: '',
        name: 'playReady',
        component: playReady
      },
      {
        path: 'play',
        name: 'play',
        component: play
      },
      {
        path: 'score',
        name: 'score',
        component: score
      }
    ]
  },
  // {
  //   path: '/play/:room_id',
  //   name: 'play',
  //   component: play
  // },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
