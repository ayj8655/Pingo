<template>
  <div>
      <div>
          <h3>코드를 입력하고 AI와 그림 퀴즈 맞춰요</h3>
      </div>
      <div>
          <input type="text" placeholder="Temporary Nickname" v-model="credentials.tmpNickname" @keydown.enter="goToLobby">
          <br>
          <button @click="goToLobby">Enter</button>
      </div>
  </div>

</template>

<script>
import axios from 'axios'
import { reactive } from 'vue'
import { useRouter } from 'vue-router'
export default {
  name: 'login',
  setup() {
    const router = useRouter()
    const credentials = reactive({
      tmpNickname: "",
    })
    const goToLobby = ()=>{
      console.log(credentials.tmpNickname)
      axios({
        method: 'GET',
        url:'',
        tmpNickname:'',
      })
      .then((res) => {
        router.push('/lobby')
      }).catch((err) => {
        console.log('닉네임 중복')
        alert('닉네임이 중복됩니다.')
        router.push('/login')
      })
      router.push('lobby')

      console.log(this.tmpNickname)
    }
    // 백엔드에 닉네임 중복인지 아닌지 요청보내기

    return {
      goToLobby,
      credentials,
      router
    }
  }


}
</script>

<style>

</style>
