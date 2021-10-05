<template>
  <div>
      <div>
        <h1>Game Ranking</h1>
      </div>
      <div>
          <button @click='playAgain'>초기화면으로</button>
          <button @click='toLobby'>로비로</button>
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
    const playAgain = () => {
      store.dispatch('resetGame')
      store.dispatch('toRoom')
    }
    const toLobby = () => {
      store.dispatch('resetGame')
      router.push('/lobby')
    }
    return {
      playAgain,
      toLobby,
      router
    }
  },
  mounted () {
    // console.log(store.state.roundCnt)
    // clearTimeout()
    console.log('gameRanking mounted')
    // store.dispatch('resetGame')
    // setTimeout(this.toRoom, 5000)
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
