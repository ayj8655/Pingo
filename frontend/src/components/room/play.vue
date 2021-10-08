<template>
  <div>
    <div class="timer-keyword" >
      <h1 id="timerBox"
      style="
      margin: 0 0 0.8rem 1rem;">
      </h1>
      <h1 class="keyword-box">{{keyword}}</h1>
    </div>
    <draw @draw-ended="playEnded"/>
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

    return {
      playEnded,
      keyword
    }
  }
}

</script>

<style>
.timer-keyword{
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;

}
.keyword-box{
  margin: 0 0 0.8rem 1rem;
  background-color: white;
  padding: 3px;
  border-radius: 3px;
  color: rgb(240, 89, 89);
  font-size: 1.5rem;
}
</style>
