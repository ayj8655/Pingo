<template>
  <div>
      <h1>showEveryOne</h1>
      <br>
      <!-- 이거 왜 안되냐 ㅠㅠㅠ -->
      <ul>
        <li v-for="(img, idx) in allImage" :key='idx'>
            <img :src='img.image' :alt='img.image'>
        </li>
      </ul>
  </div>
</template>

<script>
import store from '@/store/index.js'
import axios from 'axios'

export default {
  name: 'showEveryone',
  mounted () {
    clearTimeout()
    console.log('showEveryone mounted')

    // 나중에 카테고리 수정
    axios.get('http://localhost:8000/paint_game/paints_of_round/' + this.room_id + '/banana')
      .then((res) => {
        // console.log(res)
        this.allImage.push(res.data[0])
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
    const allImage = []

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