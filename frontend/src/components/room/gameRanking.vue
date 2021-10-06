<template>
  <div>
      <div>
        <h1>Game Ranking</h1>
      </div>
      <div>
        <ul>
          <li v-for="(data, idx) in rankingData" :key="idx">
            {{idx+1}}. {{data.user.user_name}}님의 점수: {{data.score}}
          </li>
        </ul>
      </div>
      <div>
          <button @click='playAgain'>초기화면으로</button>
          <button @click='toLobby'>로비로</button>
      </div>
  </div>
</template>

<script>
import store from '@/store/index.js'
import { onMounted, ref } from '@vue/runtime-core'
import axios from 'axios'
import { domain } from '@/domain.js'
// import { useRouter } from 'vue-router'

export default {
  name: 'gameRanking',
  setup (props, { emit }) {
    // const router = useRouter()
    const rankingData = ref([])

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
    const getRankingData = () => {
      const roomId = localStorage.getItem('room_id')
      const userName = localStorage.getItem('user_name')
      axios({
        method: 'POST',
        url: domain + '/paint_game/game_end/',
        data: {
          room_id: roomId,
          user_name: userName
        }
      })
        .then((res) => {
          // rankingData.value.push(res.data)
          rankingData.value = Array.from(res.data)
          console.log(rankingData.value)
        })
        .catch((err) => {
          console.dir(err)
        })
    }

    onMounted(() => {
      // console.log('gameRankingMounted')
      getRankingData()
    })

    return {
      playAgain,
      toLobby,
      getRankingData,
      rankingData
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
