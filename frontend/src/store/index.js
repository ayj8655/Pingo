import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    keywords: ['banana', 'blub', 'calculator', 'carrot', 'clock'],
    playState: 'playReady',
    roundCnt: 3
  },
  mutations: {
    SET_PLAYSTATE (state) {
      if (state.playState === 'playReady') {
        state.playState = 'play'
      }
      else if (state.playState === 'play') {
        state.playState = 'roundEnd'
      }
      else if (state.playState === 'roundEnd') {
        state.playState = 'showEveryone'
      }
      else if (state.playState === 'showEveryone') {
        state.playState = 'score'
      }
      else if (state.playState === 'score') {
        state.playState = 'playReady'
      }
      else {

      }
    },
    SET_ROUNDCNT (state) {
      state.roundCnt++
    },
    RESET_GAME (state) {
      state.roundCnt = 0
      state.playState = 'playReady'
    }
  },
  actions: {
    setPlayState ({ commit }) {
      commit('SET_PLAYSTATE')
    },
    increaseRoundcnt ({ commit }) {
      commit('SET_ROUNDCNT')
    },
    resetGame ({ commit }) {
      commit('RESET_GAME')
    }
  },
  modules: {
  },
  getters: {
    getPlayState: state => {
      return state.playState
    }
  }
})
