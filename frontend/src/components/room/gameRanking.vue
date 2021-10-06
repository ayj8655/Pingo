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
// import { useRouter } from 'vue-router'

export default {
  name: 'gameRanking',
  setup (props, { emit }) {
    // const router = useRouter()
    const playAgain = () => {
      // store.dispatch('toRoom')

      // store.dispatch('resetGame')
      emit('gameranking-ended', {
        choice: 'playAgain'
      })
    }
    const toLobby = () => {
      // router.push('/lobby')
      // store.dispatch('resetGame')
      emit('gameranking-ended', {
        choice: 'toLobby'
      })
    }
    return {
      playAgain,
      toLobby
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
  }
}
</script>

<style>

</style>
