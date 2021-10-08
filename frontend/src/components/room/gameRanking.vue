<template>
  <div>
    <div>
      <audio src=""></audio>
    </div>
      <div>
        <h1>Game Ranking</h1>
      </div>
      <!-- <div>
        <ul>
          <li v-for="(data, idx) in rankingData" :key="idx">
            {{idx+1}}등 {{data.user.user_name}}님의 점수: {{data.score}}
          </li>
        </ul>
      </div> -->
      <div>
          <button id="yellow-button" @click='playAgain'>대기실로</button>
          <button id="blue-button" @click='toLobby'>로비로</button>
      </div>
      <div style="width:100% height:200px overflow:auto">
        <table>
          <!-- table header -->
          <thead>
            <tr>
              <th>등수</th>
              <th>닉네임</th>
              <th>총 점수</th>
              <th>평균 점수</th>
            </tr>
          </thead>
          <!-- 출력 시작 -->
          <tbody>
            <tr v-for="(data, idx) in rankingData" :key="idx">
              <td>{{idx+1}}등</td>
              <td>{{data.user.user_name}}</td>
              <td>{{data.score.toFixed(3)}}</td>
              <td>{{(data.score/this.$store.state.keywords.length).toFixed(3)}}</td>
            </tr>
          </tbody>
        </table>
      </div>
  </div>
</template>

<script>
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
table {
    width: 100%;
    border-top: 1px solid #444444;
    border-collapse: collapse;
  }
  th, td {
    border-bottom: 1px solid #444444;
    padding: 10px;
    text-align: center;
  }
  thead tr {
    background-color: #595959;
    color: #ffffff;
  }
  tbody tr:nth-child(2n) {
    background-color: #f2f2f2;
  }
  tbody tr:nth-child(2n+1) {
    background-color: #ffdd65;
  }

</style>
