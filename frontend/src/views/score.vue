<template>
<h1>{{score}}</h1>
<h1>AI는 당신의 그림을 "{{classes}}"(으)로 예측했습니다.</h1>

</template>

<script>
import { onMounted, ref } from '@vue/runtime-core'
import axios from 'axios'

export default {
  setup() {
    const score = ref({})
    const classes = ref({})
    onMounted(() => {
      axios({
        method: 'POST',
        url: "http://localhost:8000/paint_game/ayj",
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
    })
    return {
      score,
      onMounted,
      classes
    }
  }
}
</script>

<style>

</style>