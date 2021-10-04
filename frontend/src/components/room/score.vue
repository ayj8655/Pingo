<template>
<h1>{{score}}</h1>
<h1>AI는 당신의 그림을 "{{classes}}"(으)로 예측했습니다.</h1>

</template>

<script>
import { onMounted, ref } from '@vue/runtime-core'
import axios from 'axios'
import store from '@/store/index.js'
import { useRouter } from 'vue-router'

export default {
  name: 'score',
  setup () {
    const router = useRouter()
    const score = ref({})
    const classes = ref({})

    onMounted(() => {
      clearTimeout()
      console.log('score mounted')

      axios({
        method: 'POST',
        url: "http://localhost:8000/paint_game/ayj/",
        data: {
          'user_name':localStorage.getItem('user_name'),
          'room_id':localStorage.getItem('room_id'),
          'category': 'banana' //여기 나중에 수정
        }
      })
        .then((res) => {
          console.log(res.data)
          score.value = res.data.score
          classes.value = res.data.class_name
        })
        .then(() => {
          setTimeout(toNextLevel, 5000)
        })
    })

    const toNextLevel = () => {
      store.dispatch('increaseRoundcnt')
      console.log('roundcount', store.state.roundCnt)

      if (store.state.roundCnt >= 5) {
        store.dispatch('resetGame')
        const room = localStorage.getItem('room_id')
        console.log(room)
        router.push({ name: 'room', params: { room_id: room } })
      }
      else {
        store.dispatch('setPlayState')
        console.log('to nxt level', store.state.playState)
      }
    }
    return {
      onMounted,
      toNextLevel,
      score,
      classes
    }
  },
  // mounted () {
  //   console.log('score mounted')
  //   store.dispatch('increaseRoundcnt')
  //   console.log(store.state.roundCnt)
  //   setTimeout(this.toNextLevel, 5000)
  // },
  unmounted () {
    clearTimeout()
  }
}
</script>

<style>

</style>
