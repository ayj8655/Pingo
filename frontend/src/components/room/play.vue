<template>
  <div>
      <h2 id="timerBox"></h2>
      <div>
        <h3>{{keyword}}</h3>
        <draw @draw-ended="playEnded"/>
      </div>
  </div>
</template>

<script>
import draw from '@/components/room/draw.vue'
import { onMounted, onBeforeUnmount, ref } from '@vue/runtime-core'
import { useStore } from 'vuex'

export default {
  name: 'play',
  components: { draw },
  emits: 'playEnded',

  setup (props, { emit }) {
    const store = useStore()
    var roundCnt = store.state.roundCnt
    const keyword = store.state.keywords[roundCnt]

    const playEnded = () => {
      emit('playEnded')
    }

    onMounted(() => {
      const settime = ref(1590)
      const sec = ref(0)
      const timer = setInterval(function () {
        sec.value = parseInt(settime.value / 100)

        document.getElementById('timerBox').innerHTML = '남은시간: ' + sec.value + '초'
        settime.value -= 10
        if (settime.value <= 0) {
          document.getElementById('timerBox').innerHTML = ''
          clearInterval(timer)
        }
      }, 100)
    })

    onBeforeUnmount((timer) => {
      clearInterval(timer)
    })

    return {
      playEnded,
      keyword
    }
  }
}

</script>

<style>

</style>
