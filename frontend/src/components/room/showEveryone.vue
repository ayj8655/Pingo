<template>
<div>
  <h1>모두의 그림</h1>
</div>
<div class="image-box">
    <br>
    <ul>
      <li class="list-item" v-for="(img, idx) in allImage" :key='time_now + idx'>

        <!-- <p>http://localhost:8000/{{img.image}}</p> -->
          <p>{{img.user.user_name}}</p>
          <img  :src='domain + img.image' alt='???'>
          <!-- style="height: 125px; width:125px;" -->
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
          if(this.allImage.length > 6){
            isSmall.value = !isSmall.value
          }
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
    // require('@/assets/logo.png'), require('@/assets/logo.png'), require('@/assets/logo.png'), require('@/assets/logo.png'),
    // require('@/assets/logo.png'), require('@/assets/logo.png'), require('@/assets/logo.png'), require('@/assets/logo.png'),
    // require('@/assets/logo.png'), require('@/assets/logo.png'), require('@/assets/logo.png'), require('@/assets/logo.png'),
    // require('@/assets/logo.png'), require('@/assets/logo.png'), require('@/assets/logo.png'), require('@/assets/logo.png'),
    // require('@/assets/logo.png'), require('@/assets/logo.png'), require('@/assets/logo.png'), require('@/assets/logo.png'),
    const isSmall = ref([true])
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
      showEveryoneEnded,
      isSmall
    }
  }
}
</script>

<style>
ul{
  list-style: none;
}

.list-item {
  display: flex;
  height: 200px;
  width: 200px;
  /* flex-basis: 200px; */
  float: left;
  margin: 20px;
}
.list-item2 {
  display: flex;
  height: 100px;
  width: 100px;

}


.image-box {
  overflow: scroll;
  display: flex;
  flex-direction: column;
  max-height: 800px;
  max-width: 800px;
  flex-shrink: 1;
  /* margin-top: 30px; */
}
</style>
