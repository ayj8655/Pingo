import { createStore } from 'vuex'
// import axios from 'axios'

export default createStore({
  state: {
    // user: {
    //   username: '',
    //   user_id: -1
    // }
    lobbySocket: new WebSocket('ws://J5B307.p.ssafy.io:8000/ws/game/lobby/'),
    // lobbySocket: new WebSocket('ws://localhost:8000/ws/game/lobby/'),
    roomSocket: {},
    keywords: ['banana', 'blub', 'calculator', 'carrot', 'clock'],
    playState: 'playReady',
    roundCnt: 0
  },
  mutations: {
    roomSocketConnect (state, roomId) {
      state.roomSocket = new WebSocket('ws://J5B307.p.ssafy.io:8000/ws/game/' + roomId + '/')
    },
    SET_PLAYSTATE (state) {
      if (state.roundCnt >= state.keywords.length) {
        state.playState = 'gameRanking'
      }
      if (state.playState === 'playReady') {
        state.playState = 'play'
      } else if (state.playState === 'play') {
        state.playState = 'roundEnd'
      } else if (state.playState === 'roundEnd') {
        state.playState = 'showEveryone'
      } else if (state.playState === 'showEveryone') {
        state.playState = 'score'
      } else if (state.playState === 'score') {
        state.playState = 'playReady'
      } else {

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
    lobbySend: function (context, payload) {
      context.state.lobbySocket.send(JSON.stringify(payload))
    },
    roomSend: function (context, payload) {
      context.state.roomSocket.send(JSON.stringify(payload))
    },
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
