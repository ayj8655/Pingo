import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    // user: {
    //   username: '',
    //   user_id: -1
    // }
    lobbySocket: new WebSocket('ws://localhost:8000/ws/game/lobby/')
  },
  mutations: {
  },
  actions: {
    lobbySend: function (context, payload) {
      context.state.lobbySocket.send(JSON.stringify(payload))
    }
  },
  modules: {
  }
})
