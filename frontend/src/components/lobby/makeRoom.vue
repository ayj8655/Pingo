<template>
  <div id="create-room-box">
    <div id="room-making-box" >

      <input type="text" placeholder="방 이름" v-model="data.room_name" />

      <input
        type="number"
        placeholder="0명"
        min="0"
        max="100"
        v-model="data.max_head_counts"
      />

      <input type="number" placeholder="라운드" v-model="data.problems" />
      <div class="check-box">
        <label for="">비밀방?</label>
        <input class="check-input" type="checkbox" @click="togglePassword" v-model="data.is_locked" />
      </div>
      <input type="password" placeholder="비밀번호" v-model="data.room_password" />
      <button id="blue-button" style="width: 15.5rem" @click="roomMaking">방 만들기</button>
    </div>
  </div>
</template>

<script>
import { reactive, ref } from '@vue/reactivity'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'
import { domain } from '@/domain.js'
export default {
  name: 'makeRoom',

  setup (props, { emit }) {
    const username = localStorage.getItem('user_name')
    const store = useStore()
    const data = reactive({
      room_id: '',
      room_owner: username,
      room_name: '',
      room_password: '',
      problems: '',
      max_head_counts: '',
      is_locked: false,
      is_started: false
    })
    const router = useRouter()
    const secret = ref(false)
    // const isShow = props.isShow
    const togglePassword = () => {
      data.is_locked = !data.is_locked
    }
    const roomMaking = () => {
      axios({
        method: 'POST',
        url: domain + '/paint_game/make_room/',
        data: {
          room_name: data.room_name,
          room_owner: data.room_owner,
          room_password: data.room_password,
          problems: data.problems,
          max_head_counts: data.max_head_counts,
          is_locked: data.is_locked,
          is_started: false
        }
        // 보류 socket
      })
        .then((res) => {
          // 방번호로 보내기
          store.dispatch('lobbySend',
            {
              space: 'lobby',
              req: 'getRoomList'
            }
          )
          // console.log('res.data', res.data)
          const room_id = res.data.room_id
          // console.log('방장', data.room_owner)
          const roomOwner = data.room_owner
          store.dispatch('setRoomOwner', { is_owner: true, name: roomOwner })
          router.push({ name: 'room', params: { room_id: room_id, password: data.room_password } })
        })
        .catch((err) => {
          alert('방만들기 실패')
          console.log(err)
        })
    }
    return {
      data,
      secret,
      togglePassword,
      roomMaking
    }
  }
}
</script>

<style>
#create-room-box{
  display: flex;
  justify-content: center;
  background-color: #FFF9BA;
  height: 500px;
}
#room-making-box{
  display: flex;
  justify-content: center;
  flex-direction: column;
  background-color: #fff;
  /* border: 1px black solid; */
  width: 22rem;
  height: 25rem;
  border-radius: 5px;
  margin: auto;
}
#room-making-box input {
  width: 15rem;
  height: 2rem;
  border-radius: 5px;
  margin: auto;
  margin-bottom: 0.5rem;
  cursor: pointer;
  border: 0.5px gray solid;
}
#room-making-box p {
  margin: 0.1rem;
  font-size: 0.8rem;
  font-weight: bold;
}
#room-making-box label {
  margin: 0.1rem;
  font-size: 0.8rem;
  font-weight: bold;
}
#room-making-box button {
  margin: auto;
}

.check-box{
  display: flex;
  justify-content: center;
  margin-top: 0.5rem;

}
.check-input{
  height:1.5rem !important;
  width:1.5rem !important;
  margin: 0 !important;
  margin-left: 1rem !important;
  cursor: pointer;
  /* margin-bottom: 1rem !important; */
}
</style>
