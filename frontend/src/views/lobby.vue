<template>
    <div id="back" class="lobby-frame">
      <!-- <div> <h3>Lobby</h3></div> -->
      <section class="lobby-left-box">
        <section>
          <button id="yellow-button" @click="createRoom">방만들기</button>
        </section>
        <section class="lobby-left">
          <div v-for="user in userList" :key="user.user_id">
            <p>{{user.user_name}}</p>
          </div>
        </section>
        <div id="audio-box">
          <audio controls autoplay loop src="/victory.m4a" type="audio.m4a">
            <source >
          </audio>
        </div>

      </section>
      <section class="lobby-right">
        <!-- <h1>오른쪽</h1> -->
        <!-- <h1>{{roomList}}</h1> -->
        <ul>
          <roomItem v-for="room in roomList"
          :key='room.room_id'
          :room='room'
          @click="moveRoom(room)"/>
        </ul>
      </section>
      <section>
        <Modal :isShow='isShow' @switchModal='switchModal'>
          <template v-slot:header>
          </template>
          <template v-slot:body>
            <div v-if="roomMaking">
              <makeRoom/>
            </div>
            <div v-if="password && isLocked">
              <h1>비번입력</h1>
              <lockRoom />
            </div>
          </template>
          <template v-slot:footer>
          </template>
        </Modal>
      </section>
    </div>
</template>

<script>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import makeRoom from '../components/lobby/makeRoom.vue'
import lockRoom from '../components/lobby/lockRoom.vue'
import roomItem from '../components/lobby/roomItem.vue'
import Modal from '@/components/Modal.vue'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'
import store from '@/store/index.js'

export default {
  name: 'Lobby',
  components: {
    makeRoom,
    Modal,
    roomItem,
    lockRoom

  },
  setup () {
    const router = useRouter()
    const store = useStore()
    var roomList = ref([])
    const userList = ref([])
    const isShow = ref(false)
    const roomMaking = ref(false)
    const isLocked = ref(false)
    const password = ref(false)
    const lobbySocket = store.state.lobbySocket

    const getUserList = () => {
      store.dispatch('lobbySend',
        {
          space: 'lobby',
          req: 'getUserList'
        }
      )
    }

    const switchModal = () => {
      isShow.value = !isShow.value
      console.log(roomMaking.value, password.value, isLocked.value)
      if (roomMaking.value === true) { roomMaking.value = !roomMaking.value }
      if (password.value === true) { password.value = !password.value }
      if (isLocked.value === true) { isLocked.value = !password.value }
    }

    const createRoom = () => {
      isShow.value = !isShow.value
      roomMaking.value = !roomMaking.value
    }

    const moveRoom = (room) => {
      store.dispatch('resetGame')
      localStorage.setItem('room_id', room.room_id)
      if (room.is_started === true) {
        alert('게임이 진행중일 때는 입장할 수 없습니다.')
      } else if (room.is_locked === true) {
        (isLocked.value = true) && (isShow.value = !isShow.value) && (password.value = !password.value)
      } else {
        router.push({ name: 'room', params: { room_id: room.room_id } })
      }
    }

    lobbySocket.onmessage = (e) => {
      const data = JSON.parse(e.data)
      console.log('lobby 68line', data)
      if (data.res === 'getUserList') {
        userList.value = data.value
      } else if (data.res === 'getRoomList') {
        roomList.value = data.value
      }
    }
    lobbySocket.onopen = () => {
      getUserList()
    }

    onMounted(() => {
      if (lobbySocket.readyState === 1) {
        getUserList()
      }
      axios({
        method: 'GET',
        url: '/paint_game/room_list/'
      }).then((res) => {
        roomList.value = res.data
      }).catch((err) => {
        console.dir(err)
      })
    })

    return {
      roomList,
      createRoom,
      isShow,
      isLocked,
      password,
      switchModal,
      userList,
      roomItem,
      moveRoom,
      roomMaking
    }
  }
}
</script>

<style scoped>
.lobby-frame {
  box-sizing: border-box;
    min-height: 600px;
    min-width: 900px;
    flex-grow: 1;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 35px 40px;
    padding-top: 15px !important;
}

.lobby-left-box{
  display: flex;
  flex-direction: column;
}

.lobby-left{
  background-color: white;
  max-width: 400px;
  flex-basis: 400px;
  flex: 1 1 100%;
  box-sizing: border-box;
  border-radius: 5px;
  margin: 10px;
}

.lobby-right{
  background-color: white;
  flex-basis: 100px;
  flex: 1 1 100%;
  box-sizing: border-box;
  border-radius: 5px;
  margin: 10px;
  display: flex;
  justify-content: space-between;
}
</style>
