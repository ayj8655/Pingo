<template>
  <div class="lock-room-box">
    <div id="lock-room-box">
      <img style="height:250px; width: 300px; margin-top:30px" src="/lock2.png" alt="lock">
      <input class="lock-input" type="password" placeholder="password" v-model="password">
      <button id="blue-button" @click="enterRoom">입장</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { useRouter } from 'vue-router'
import { domain } from '@/domain.js'
import { ref } from '@vue/reactivity'
export default {
  setup () {
    const password = ref('')
    const room_id = parseInt(localStorage.getItem('room_id'))
    const user_id = parseInt(localStorage.getItem('user_id'))
    const router = useRouter()
    const enterRoom = () => {
      console.log(typeof(user_id), user_id)
      console.log(typeof(room_id), room_id)
      console.log(typeof(password.value), password.value)
      axios.post(domain + '/paint_game/enter_room/', {
        user_id: user_id,
        room_id: room_id,
        room_password: password.value
      })
      .then((res) => {
        console.log(res)
        // router.push({ name: 'room', params: { room_id: room_id } })
        router.push({ name: 'room', params: { room_id: room_id, password: password.value } })
      })
      .catch((err) => {
        alert('비밀번호가 틀립니다')
        router.push('/lobby')
      }

      )
    }

    return {
      password,
      enterRoom
    }
  }
}
</script>

<style>
.lock-room-box{
  height: 400px;
  width: 300px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: auto;

}

#lock-room-box{

  background-color:#FFF9BA;
  margin: auto;
  display: flex;
  align-items: center;
  flex-direction: column;


}


.lock-input{
  height: 3rem;
  width: 16.8rem;
  border: none;
  border-radius: 5px;
  font-size: 1.5rem;
  margin-top: 2rem;
  margin-bottom: 0.5rem;
  padding-left: 1rem;
}
</style>
