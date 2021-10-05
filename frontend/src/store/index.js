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
    keywords: [],
    playState: 'playReady',
    roundCnt: 0,
    isStarted: false,
    gameEnded: false
  },
  mutations: {
    roomSocketConnect (state, roomId) {
      state.roomSocket = new WebSocket('ws://J5B307.p.ssafy.io:8000/ws/game/' + roomId + '/')
      // state.roomSocket = new WebSocket('ws://localhost:8000/ws/game/' + roomId + '/')
    },
    SET_PLAYSTATE (state) {
      if (state.gameEnded === true) {
        state.playState = 'gameRanking'
      } else if (state.playState === 'playReady') {
        state.playState = 'play'
      } else if (state.playState === 'play') {
        state.playState = 'roundEnd'
      } else if (state.playState === 'roundEnd') {
        state.playState = 'showEveryone'
      } else if (state.playState === 'showEveryone') {
        state.playState = 'score'
      } else if (state.playState === 'score') {
        state.playState = 'playReady'
      }
      console.log(state.playState)
    },
    SET_ROUNDCNT (state) {
      state.roundCnt++
    },
    RESET_GAME (state) {
      state.roundCnt = 0
      state.playState = 'playReady'
      state.gameEnded = false
    },
    END_GAME (state) {
      state.gameEnded = true
    },
    START_GAME (state) {
      state.isStarted = true
    },
    TO_ROOM (state) {
      state.isStarted = false
    },
    setKeywords (state, payload) {
      state.keywords = payload.map((e) => e.category)
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
    },
    endGame ({ commit }) {
      commit('END_GAME')
    },
    startGame ({ commit }) {
      commit('START_GAME')
    },
    toRoom ({ commit }) {
      commit('TO_ROOM')
    }
  },
  modules: {
  },
  getters: {
    getPlayState: state => {
      return state.playState
    },
    getIsStarted: state => {
      return state.isStarted
    }
  }
})
