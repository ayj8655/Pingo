<template>
  <div>
      <h1>showEveryOne</h1>
      <br>
      <!-- 이거 왜 안되냐 ㅠㅠㅠ -->
      <ul>
        <li v-for="(img, idx) in allImage" :key='idx'>
          <!-- <p>http://localhost:8000/{{img.image}}</p> -->
            <img :src='"http://localhost:8000"+img.image' alt='???'>
        </li>
      </ul>
  </div>
</template>

<script>
import store from '@/store/index.js'
import axios from 'axios'
import { ref } from '@vue/reactivity'


export default {
  name: 'showEveryone',
  mounted () {
    clearTimeout()
    console.log('showEveryone mounted')

    // 나중에 카테고리 수정
    const roundCnt = store.state.roundCnt
    const category = store.state.keywords[roundCnt]
    axios.get('/paint_game/paints_of_round/' + this.room_id + '/' + category)
      .then((res) => {
        // console.log(res)
        this.allImage = res.data
        console.log('allimage', this.allImage)
      })
      .then(() => {
        setTimeout(this.toNextLevel, 3000)
      })
      .catch((err) => {
        console.log(err)
      })
  },

  unmounted () {
    clearTimeout()
  },

  setup () {
    const room_id = localStorage.getItem('room_id')
    const allImage = ref([])

    const toNextLevel = () => {
      store.dispatch('setPlayState')
      console.log('to nxt level', store.state.playState)
    }

    return {
      toNextLevel,
      room_id,
      allImage
    }
  }
}
</script>

<style>

</style>