<template>
  <div>
      <h1>play</h1>
      <div>
        <draw/>
      </div>
      <div>
        <chating/>
      </div>
  </div>
</template>

<script>
import draw from '@/components/room/draw.vue'
import chating from '@/components/room/chating.vue'

export default {
  name: 'play',
  components: { draw, chating },
  // mounted () {
  //   console.log('play mounted')
  //   setTimeout(this.toPlay, 3000)
  // },
  // setup() { 
  //   const toPlay = () => {
  //     store.dispatch('setPlayState')
  //     console.log('to nxt level', store.state.playState)
  //   }
  //   return {
  //     toPlay
  //   }
  // }
}
</script>

<style>

</style>