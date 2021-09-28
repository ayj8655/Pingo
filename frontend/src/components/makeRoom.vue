<template>
  <div>
    <div><h3>make Room</h3></div>
    <div>
        <label for="">방 이름: </label>
        <input type="text" placeholder="방 제목" v-model="data.room_name">
        <br>
        <label for=""> 인원수: </label>
        <input type="number" placeholder="인원 제한" min="0" max="100" v-model="data.max_head_counts">
        <br>
        <label for="">판 수: </label>
        <input type="number" placeholder="몇판"  v-model="data.problems">
        <br>
        <label for="">비밀방?</label>
        <input type="checkbox" @click="togglePassword" v-model="data.is_locked">
        <br>
        <label for="">비밀번호</label>
        <input type="password" v-model="data.room_password">
        <br>
        <button id="blue-button" @click="roomMaking">방 만들기</button>
    </div>
  </div>
</template>

<script>
import { reactive, ref } from '@vue/reactivity'
import axios from 'axios'
import { useRouter } from 'vue-router'
export default {
  name: 'makeRoom',


  setup() {
    const username = localStorage.getItem('username')

    const data = reactive({
      room_id: "",
      room_owner: username,
      room_name: "",
      room_password: "",
      problems: "",
      max_head_counts: "",
      is_locked: "",
      is_started: false,
    })
    console.log('data', data)
    const router = useRouter()
    const secret = ref(false)
    // const isShow = props.isShow
    const togglePassword = () => {
      data.is_locked.value = !data.is_locked.value
    }
    const roomMaking = () => {
      console.log('data', data)
      axios({
        method: 'POST',
        url: 'http://localhost:8000/paint_game/make_room/',
        data:{
          room_name: data.room_name,
          room_owner: localStorage.username,
          room_password: data.room_password,
          problems: data.problems,
          max_head_counts: data.max_head_counts,
          is_locked: data.is_locked,
          is_started: false,
        }

        // 보류 socket

      }).then((res)=>{
        // 방번호로 보내기
        // router.push('')
      }).catch((err)=>{
        console.log("방만들기 실패")
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

</style>
