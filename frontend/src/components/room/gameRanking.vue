<template>
  <div>
      <div>
        <h1>Game Ranking</h1>
      </div>
      <div>
          <button>Again?</button>
          <button>Exit</button>
      </div>
  </div>
</template>

<script>
import store from '@/store/index.js'
import { useRouter } from 'vue-router'

export default {
  name: 'gameRanking',
  setup () {
    const router = useRouter()
    const toRoom = () => {
      const room = localStorage.getItem('room_id')
      router.push({ name: 'room', params: { room_id: room.room_id } })
    }
    return {
      toRoom,
      router
    }
  },
  mounted () {
    console.log(store.state.roundCnt)
    clearTimeout()
    console.log('gameRanking mounted')
    store.dispatch('resetGame')
    setTimeout(this.toRoom, 5000)
    // const router = useRouter()
    // router.push()
  },
  unmounted () {
    clearTimeout()
  },
}
</script>

<style>

</style>
