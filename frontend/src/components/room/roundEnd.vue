<template>
<div class="score-board">
  <div class="score-box">
      <h1>분석중입니다</h1>
  </div>
</div>
</template>

<script>
import store from '@/store/index.js'

export default {
  name: 'roundEnd',
  mounted () {
    clearTimeout()
    // console.log('roundEnd mounted')
    setTimeout(this.toNextLevel, 3000)
  },
  unmounted () {
    clearTimeout()
  },
  setup (props, { emit }) {
    const toNextLevel = () => {
      // store.dispatch('setPlayState')
      roundEndEnded()
      // console.log('to nxt level', store.state.playState)
    }

    const roundEndEnded = () => {
      emit('roundend-ended')
    }

    return {
      toNextLevel,
      roundEndEnded
    }
  }
}
</script>

<style>
</style>
