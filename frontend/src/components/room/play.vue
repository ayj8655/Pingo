<template>
  <div>
    <div >
      <h1 id="timerBox"
      style="
      margin-top: 0;
      margin-bottom: 0.8rem !important">
      </h1>
      <div>
        <draw @draw-ended="playEnded"/>
      </div>
    </div>
  </div>
</template>

<script>
import draw from '@/components/room/draw.vue'
import chating from '@/components/room/chating.vue'
import { onMounted, onBeforeUnmount, ref } from '@vue/runtime-core'

export default {
  name: 'play',
  components: { draw, chating },
  emits: 'playEnded',

  setup (props, {emit}) {
    onMounted(()=> {

      const settime = ref(1510)
      const sec = ref(0)

      const timer = setInterval(function () {
        sec.value = parseInt(settime.value / 100)

        document.getElementById('timerBox').innerHTML = '남은시간: ' + sec.value + '초'
        settime.value -= 10
        if (settime.value <= 0) {

          clearInterval(timer)
          document.getElementById('timerBox').innerHTML = '종료'
        }
        }, 100)


    })
    onBeforeUnmount((timer) => {
      clearInterval(timer)
    })
    const playEnded = () => {
      emit('playEnded')
    }

    return {
      setTimeout,
      playEnded
    }
  } }

</script>

<style>

</style>
