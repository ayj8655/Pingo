<template>
<h1>{{score}}</h1>

</template>

<script>
import { onMounted, ref } from '@vue/runtime-core'
import axios from 'axios'

export default {
setup(){

  const score = ref({})
  onMounted(() => {
    axios({
      method: 'GET',
      url: "http://localhost:8000/paint_game/ayj"

    })
    .then((res) => {
      console.log(res.data)
      score.value = res.data.score
    })
  })
  return {
    score,
    onMounted
  }
}
}
</script>

<style>

</style>