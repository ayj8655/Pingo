<template>
  <div class="image-box">
      <h1>모두의 그림</h1>
      <br>
      <ul>
        <li class="list-item" v-for="(img, idx) in allImage" :key='time_now + idx'>
          <!-- <p>http://localhost:8000/{{img.image}}</p> -->
            <p>{{key}}</p>
            <img :src='domain+img.image' alt='???'>
            <!-- <p>{{img.image}}</p> -->
        </li>
      </ul>
  </div>
</template>

<script>
import store from '@/store/index.js'
import axios from 'axios'
import { ref } from '@vue/reactivity'
import { domain } from '@/domain.js'


export default {
  name: 'showEveryone',
  mounted () {
    clearTimeout()
    console.log('showEveryone mounted')
    // 나중에 카테고리 수정
    const roundCnt = store.state.roundCnt
    const category = store.state.keywords[roundCnt]
    axios.get(domain + '/paint_game/paints_of_round/' + this.room_id + '/' + category)
      .then((res) => {
        this.allImage = res.data
        console.log('이거확인', this.allImage)
        // console.log('allimage', this.allImage)
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

  setup (props, { emit }) {
    const room_id = localStorage.getItem('room_id')
    const allImage = ref([])
    const time_now = Date.now()
    const toNextLevel = () => {
      // store.dispatch('setPlayState')
      showEveryoneEnded()
      console.log('to nxt level', store.state.playState)
    }

    const showEveryoneEnded = () => {
      emit('showeveryone-ended')
    }

    return {
      toNextLevel,
      room_id,
      allImage,
      time_now,
      domain,
      showEveryoneEnded
    }
  }
}
</script>

<style>
ul{
  list-style: none;
}

.list-item {
  display: inline-box;
  height: 100px;
  width: 100px;
}

.image-box {
  overflow: scroll;
}
</style>
