<template>
    <!-- <slot name="playReady" :childData='childData' :close='close'> -->
  <div class="score-board">
    <div class="score-box">
        <h1>Are you Ready?</h1>
        <h3>{{this.roundCnt+1}} 라운드 </h3>
        <h1 class="class-word">"{{keyword}}"</h1>
    </div>
  </div>
    <!-- </slot> -->
</template>

<script>
// import {onMounted} from 'vue'
import store from '@/store/index.js'
export default {
  name: 'ready',
  mounted () {
    // console.log('isStarted', store.state.isStarted)
    // console.log('라운드', store.state.roundCnt)
    // console.log('상태', store.state.playState)
    clearTimeout()
    // console.log('playReady mounted')
    // store.dispatch('resetGame')
    setTimeout(this.toNextLevel, 3000)
  },
  unmounted () {
    clearTimeout()
  },
  setup (props, { emit }) {
    var roundCnt = store.state.roundCnt
    const keyword = store.state.keywords[roundCnt]
    const toNextLevel = () => {
      // store.dispatch('setPlayState')
      // console.log('to nxt level', store.state.playState)
      emit('playready-ended')
    }
    return {
      toNextLevel,
      roundCnt,
      keyword
    }
  }
}
</script>

<style>
.class-word{
  font-size: 4rem;
  color: rgb(240, 89, 89);
}
</style>
