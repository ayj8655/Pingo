<template>
    <slot name="playReady" :childData='childData' :close='close'>
  <div>

      <h1>playReady</h1>
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
    console.log(store.state.roundCnt)
    clearTimeout()
    console.log('playReady mounted')
    store.dispatch('resetGame')
    setTimeout(this.toNextLevel, 3000)
  },
  unmounted () {
    clearTimeout()
  },
  setup () {
    const roundCnt = store.state.roundCnt
    const keyword = store.state.keywords[roundCnt]
    const toNextLevel = () => {
      store.dispatch('setPlayState')
      console.log('to nxt level', store.state.playState)
    }
    return {
      toNextLevel,
      keyword
    }
  }
}
</script>

<style>

</style>