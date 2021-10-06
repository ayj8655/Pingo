<template>
<h1>{{score}}</h1>
<h1>AI는 당신의 그림을 "{{classes}}"(으)로 예측했습니다.</h1>

</template>

<script>
import { onMounted, ref } from '@vue/runtime-core'
import axios from 'axios'
import store from '@/store/index.js'
import { useRouter } from 'vue-router'
import { domain } from '@/domain.js'

export default {
  name: 'score',
  setup (prop, { emit }) {
    const router = useRouter()
    const score = ref({})
    const classes = ref({})

    onMounted(() => {
      clearTimeout()
      // console.log('score mounted')
      const roundCnt = store.state.roundCnt
      const category = store.state.keywords[roundCnt]

      axios({
        method: 'POST',

        url: domain + "/paint_game/ayj/",
        data: {
          'user_name':localStorage.getItem('user_name'),
          'room_id':localStorage.getItem('room_id'),
          'category': category
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

    const scoreEnded = () => {
      emit('score-ended')
    }

    const toNextLevel = () => {
      store.dispatch('increaseRoundcnt')
      scoreEnded()
      // console.log('roundcount', store.state.roundCnt)
      // console.log('len keyword', store.state.keywords.length)

      // if (store.state.roundCnt >= store.state.keywords.length) {
      //   store.dispatch('endGame')
      // }
      // store.dispatch('setPlayState')
      // console.log('to nxt level', store.state.playState)
    }
    return {
      onMounted,
      toNextLevel,
      scoreEnded,
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
