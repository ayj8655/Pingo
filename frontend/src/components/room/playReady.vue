<template>
    <slot name="playReady" :childData='childData' :close='close'>
  <div>

      <h1>playReady</h1>
      <h3>라운드 {{this.roundCnt+1}}</h3>
      <p>{{keyword}}</p>
  </div>
    </slot>
</template>

<script>
// import {onMounted} from 'vue'
import store from '@/store/index.js'
export default {
  name: 'ready',

  mounted () {
    console.log('라운드', store.state.roundCnt)
    console.log('상태', store.state.playState)
    clearTimeout()
    console.log('playReady mounted')
    // store.dispatch('resetGame')
    setTimeout(this.toNextLevel, 3000)
  },
  unmounted () {
    clearTimeout()
  },
  setup () {
    var roundCnt = store.state.roundCnt
    const keyword = store.state.keywords[roundCnt]
    const toNextLevel = () => {
      store.dispatch('setPlayState')
      console.log('to nxt level', store.state.playState)
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

</style>