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
          <playReady @playready-ended="playReadyEnded"/>
        </div>
        <div v-else-if='playState === "play"'>
          <play @play-ended="playEnded"/>
        </div>
        <div v-else-if='playState === "roundEnd"'>
          <roundEnd @roundend-ended="roundEndEnded"/>
        </div>
        <div v-else-if='playState === "showEveryone"'>
          <showEveryone @showeveryone-ended="showEveryoneEnded"/>
        </div>
        <div v-else-if='playState === "score"'>
          <score @score-ended="scoreEnded"/>
        </div>
        <div v-else-if='playState === "gameRanking"'>
          <gameRanking @gameranking-ended="gameRankingEnded"/>
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
import { ref, isReactive } from 'vue'
import { useRouter } from 'vue-router'
export default {
  components: { playReady, play, roundEnd, showEveryone, score, gameRanking },

  setup (props, { emit }) {
    const playState = ref('playReady')
    console.log(isReactive(playState.value))
    // const keywords = ['banana', 'bulb', 'calculator', 'carrot', 'clock']
    // const rounds = keywords.length
    const router = useRouter()

    const playReadyEnded = () => {
      console.log('playReadyEnded')
      playState.value = 'play'
    }

    const playEnded = () => {
      playState.value = 'roundEnd'
    }

    const roundEndEnded = () => {
      playState.value = 'showEveryone'
    }

    const showEveryoneEnded = () => {
      playState.value = 'score'
    }

    const scoreEnded = () => {
      console.log('roundcnt', store.state.roundCnt)
      console.log('keyword length', store.state.keywords.length)
      if (store.state.roundCnt >= store.state.keywords.length) {
        playState.value = 'gameRanking'
      }
      else {
        playState.value = 'playReady'
      }
    }

    const gameRankingEnded = (val) => {
      console.log(val.choice)
      store.dispatch('resetGame')
      if (val.choice === 'toLobby') {
        router.push('/lobby')
      }
      else{
        emit('to-Room')
      }
    }
    // onMounted{

    // }
    // forEach(keywords)
    return {
      playReadyEnded,
      playEnded,
      roundEndEnded,
      showEveryoneEnded,
      scoreEnded,
      gameRankingEnded,
      playState,
      router
    }
  },
  // computed: {
  //   change: function () {
  //     return store.getters['getPlayState']
  //   }
  // },
  // watch: {
  //   change (value) {
  //     this.playState = value
  //   }
  // },
  mounted () {
    store.dispatch('resetGame')
    this.playState = 'playReady'
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
