<template>
<div class="score-board">
  <div class="show-everyone">
    <div class="show-image">
      <h1 class="class-word" style="font-size:3rem;">모두의 그림</h1>
    </div>
    <div class="image-box">
        <br>
      <ul>
        <li class="list-item" v-for="(img, idx) in allImage" :key='time_now + idx'>
          <span class="an-item">
            <img  :src='domain + img.image' alt='???' style="height:100px; width:100px;">
            <p>{{img.user.user_name}}</p>
          </span>
        </li>
      </ul>
    </div>
  </div>
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
        // console.log('이거확인', this.allImage)
      })
      .then(() => {
        setTimeout(this.toNextLevel, 8000)
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
  height: 100px;
  width: 100px;
  /* flex-basis: 200px; */
  float: left;
  margin: 10px;
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

.show-everyone{
  height: 500px;
  margin-top: 3rem;
  display: flex-start;
  flex-direction: column;
  background-color: rgba(255, 255, 240, 0.534);
  color: #3883BC;
  font-size: 1.2rem;
}


.show-image{

  display: flex;
  flex-direction: column;
  color: ivory;
}

.an-item{
  display: flex;
  flex-direction: column;
}
.an-item p {
  margin: 3px;
}
</style>
