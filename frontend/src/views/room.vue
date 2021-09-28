<template>

  <button id="yellow-button" @click="start(room_id)">start</button>

</template>

<script>
import {onMounted, ref} from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
export default {


  setup() {
    const router = useRouter()
    const start= ((room_id) => {
      router.push({name:'play',
                  params: {room_id: room_id }})
    })
    onMounted(()=> {
      axios({
        method: 'GET',
        url: 'http://localhost:8000/paint_game/room_member/{room_id}',

      }).then((res) => {
        console.log(roomList)
        roomList.value.push(res.data)
      }).catch((err) => {
        console.log(err)
      })
    })

    return {
      start
    }
  }
}
</script>

<style>

</style>
