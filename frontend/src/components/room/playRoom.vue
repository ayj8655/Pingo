<template>
  <div>
      <h1>playRoom</h1>
      <nav>
          <button @click='playState = "playReady"'>to playReady</button>
          <button @click='playState = "play"'>to play</button>
          <button @click='playState = "roundEnd"'>to roundEnd</button>
          <button @click='playState = "showEveryone"'>to showEveryone</button>
          <button @click='playState = "score"'>to score</button>
          <!-- <button @click='show = 2'>to play</button>
          <button @click='show = 3'>to score</button> -->
      </nav>

      <transition name='fade' mode='out-in'>
        <div v-if='playState === "playReady"'>
          <playReady/>
        </div>
        <div v-else-if='playState === "play"'>
          <play/>
        </div>
        <div v-else-if='playState === "roundEnd"'>
          <roundEnd/>
        </div>
        <div v-else-if='playState === "showEveryone"'>
          <showEveryone/>
        </div>
        <div v-else-if='playState === "score"'>
          <score/>
        </div>
        <div v-else-if='playState === "gameRanking"'>
          <gameRanking/>
        </div>
      </transition>

  </div>
</template>

<script>
import playReady from '@/components/room/playReady.vue'
import play from '@/components/room/play.vue'
import roundEnd from '@/components/room/roundEnd.vue'
import showEveryone from '@/components/room/showEveryone.vue'
import score from '@/components/room/score.vue'
import gameRanking from '@/components/room/gameRanking.vue'


// Inside of vue router, you do not have a vue instance.
// Therefore there is no way to access this.$store.state.
// In order to access your store you need to include vuex into the router.
import store from '@/store/index.js'
import { ref } from 'vue'

export default {
  components: { playReady, play, roundEnd, showEveryone, score, gameRanking },

  setup() {
    const playState = ref('playReady')
    // const keywords = ['banana', 'bulb', 'calculator', 'carrot', 'clock']
    // const rounds = keywords.length

    // onMounted{

    // }
    // forEach(keywords)
    return {
      playState
    }
  },
  computed: {
    change: function () {
      return store.getters['getPlayState']
    }
  },
  watch: {
    change (value) {
      this.playState = value
    }
  }
}
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}


.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
