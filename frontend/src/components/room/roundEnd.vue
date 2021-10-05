<template>
  <div>
      <h1>끗!</h1>
  </div>
</template>

<script>
import store from '@/store/index.js'

export default {
  name: 'roundEnd',
  mounted () {
    clearTimeout()
    console.log('roundEnd mounted')
    setTimeout(this.toNextLevel, 3000)
  },
  unmounted () {
    clearTimeout()
  },
  setup () {
    const toNextLevel = () => {
      store.dispatch('setPlayState')
      console.log('to nxt level', store.state.playState)
    }
    return {
      toNextLevel
    }
  }
}
</script>

<style>
</style>
