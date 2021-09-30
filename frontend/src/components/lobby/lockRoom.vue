<template>
  <div>
    <input type="text" v-model="password">
    <button @click="enterRoom">입장</button>
  </div>
</template>

<script>
import axios from 'axios'
import { useRouter } from 'vue-router'
export default {
  setup() {
    const password = ''
    const room_id = localStorage.getItem('room_id')
    const router = useRouter()
    const enterRoom = () => {
      axios({
        method: 'POST',
        url: "http://localhost:8000/paint_game/enter_room/",
        data: {
          user_id: localStorage.getItem('user_id'),
          room_id: room_id
        }
      }).then((res) => {
        console.log(res)
      }).then(
        router.push({name:'room',
                    params: {room_id: room_id }})
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

</style>
