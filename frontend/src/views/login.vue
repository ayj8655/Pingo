<template>
  <div id='back'>
      <div>
          <p>AI와 그림 퀴즈 맞춰요</p>
      </div>
      <div>
          <input type="text" placeholder="Temporary Nickname" v-model="credentials.user_name" @keydown.enter="goToLobby">
          <!-- <button @click="checkDuplication">중복검사</button> -->
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
  setup () {
    const router = useRouter()
    const credentials = reactive({
      user_name: ''
    })
    const checkDuplication = () => {
      console.log('아이디 중복 검사')
      // axios({
      //   method: 'POST',
      //   url: 'http://localhost:8000/accounts/check_duplication/',
      //   data: {
      //     user_name: credentials.user_name,
      //   }

      // }).then((res) => {
      //   console.log(res)
      // })
    }
    console.log('credential', credentials.user_name)

    const goToLobby = () => {
      const user = {'user_name': credentials.user_name}
      // console.log(user)
      console.log('아이디 중복 검사')
      axios({
        method: 'POST',
        url: 'http://localhost:8000/accounts/check_duplication/',
        data: {
          user_name: credentials.user_name,
        }
        }).then((res) => {


      axios({
        method: 'POST',
        url: 'http://localhost:8000/accounts/signup/',
        data: user
      }).then((res) => {
        console.log('data.data', res.data)
        localStorage.setItem('username', res.data.user_name)
        router.push('/lobby')
        }).catch((err) => {
          console.log(err)

          router.push('/login')
        })
      // router.push('lobby')

      })
      console.log(credentials.user_name)
    }
    // 백엔드에 닉네임 중복인지 아닌지 요청보내기

    return {
      goToLobby,
      credentials,
      router,
      checkDuplication
    }
  }

}
</script>

<style>

</style>
