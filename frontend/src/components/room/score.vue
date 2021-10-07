<template>
<div class="score-board">
  <div class="score-box">
    <h3>Pingo가 보기에 {{classes}}로서</h3>
    <h3>{{score2}}점 입니다</h3>
    <div v-if="flag">
      <h3>혹시 {{maxClass}}를 그린건가요?</h3>
      <h3>{{maxClass}}에 대한 점수는 {{maxScore2}}입니다</h3>
    </div>
  </div>
</div>

</template>

<script>
import { onMounted, ref } from '@vue/runtime-core'
import axios from 'axios'
import store from '@/store/index.js'
import { domain } from '@/domain.js'

export default {
  name: 'score',
  setup (prop, { emit }) {
    const score = ref('채점 중')
    const maxScore = ref('채점 중')
    const classes = ref('?')
    const maxClass = ref('?')
    const score2 = ref('채점 중')
    const maxScore2 = ref('채점 중')
    const flag = ref(false)
    onMounted(() => {
      clearTimeout()
      // console.log('score mounted')
      const roundCnt = store.state.roundCnt
      const category = store.state.keywords[roundCnt]

      axios({
        method: 'POST',
        url: domain + '/paint_game/ayj/',
        data: {
          user_name: localStorage.getItem('user_name'),
          room_id: localStorage.getItem('room_id'),
          category: category
        }
      })
        .then((res) => {
          // console.log(res.data)
          score.value = res.data.score
          classes.value = res.data.class_name
          maxScore.value = res.data.max_score
          maxClass.value = res.data.max_class
          if (maxScore.value > score.value) {
            flag.value = true
          }
          score2.value = score.value.toFixed(3)
          maxScore2.value = maxScore.value.toFixed(3)
        })
        .then(() => {
          setTimeout(toNextLevel, 5000)
        })
    })

    const scoreEnded = () => {
      emit('score-ended')
    }

    const toNextLevel = () => {
      store.dispatch('increaseRoundcnt')
      scoreEnded()
    }
    return {
      onMounted,
      toNextLevel,
      scoreEnded,
      classes,
      flag,
      maxClass,
      score2,
      maxScore2
    }
  },

  unmounted () {
    clearTimeout()
  }
}
</script>

<style>
.score-board{
  height: 600px;
  display: flex;
  margin-top: auto;
  margin-bottom: auto;
  flex-direction: column;
}

.score-box{
  height: 500px;
  margin-top: 3rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  background-color: rgba(255, 255, 240, 0.534);
  color: #3883BC;
  font-size: 1.2rem;
}
</style>
