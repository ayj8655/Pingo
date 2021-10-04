import { createStore } from 'vuex'
// import axios from 'axios'

export default createStore({
  state: {
    // user: {
    //   username: '',
    //   user_id: -1
    // }
    lobbySocket: new WebSocket('ws://localhost:8000/ws/game/lobby/'),
    roomSocket: {}
  },
  mutations: {
    roomSocketConnect (state, roomId) {
      state.roomSocket = new WebSocket('ws://localhost:8000/ws/game/' + roomId + '/')
    }
  },
  actions: {
    lobbySend: function (context, payload) {
      context.state.lobbySocket.send(JSON.stringify(payload))
    },
    roomSend: function (context, payload) {
      context.state.roomSocket.send(JSON.stringify(payload))
    }
  },
  modules: {
  }
})
