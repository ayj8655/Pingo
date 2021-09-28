<template>
<h1>{{score}}</h1>
<h1>AI는 당신의 그림을 "{{classes}}"(으)로 예측했습니다.</h1>

</template>

<script>
import { onMounted, ref } from '@vue/runtime-core'
import axios from 'axios'

export default {
setup(){

  const score = ref({})
  const classes = ref({})
  onMounted(() => {
    axios({
      method: 'GET',
      url: "http://localhost:8000/paint_game/ayj"

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
