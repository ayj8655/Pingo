<template>
  <div>
      <h2 id="timerBox">

      </h2>
      <div>
        <draw/>
      </div>
      <div>
        <chating/>
      </div>
  </div>
</template>

<script>
import draw from '@/components/room/draw.vue'
import chating from '@/components/room/chating.vue'
import { onMounted, ref } from '@vue/runtime-core'

export default {
  name: 'play',
  components: { draw, chating },
  setup(){
    onMounted(()=> {

      const settime = ref(1590)
      const sec = ref(0)

      const timer = setInterval(function () {
        sec.value = parseInt(settime.value / 100)

        document.getElementById('timerBox').innerHTML = '남은시간: ' + sec.value + '초'
        settime.value -= 10
        if (settime.value <= 0){
          clearInterval(timer)
          document.getElementById('timerBox').innerHTML = ''}
        }, 100)

    })
    return {
      setTimeout
    }
  } }

</script>

<style>

</style>
