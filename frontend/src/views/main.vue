<template>
  <div>
      <div>
          <h3>코드를 입력하고 AI와 그림 퀴즈 맞춰요</h3>
      </div>
      <div>
          <input type="text" placeholder="Temporary Nickname" v-model="this.tmpNickname" @keydown.enter="goToLobby()">
          <br>
          <button @click="goToLobby()">Enter</button>
      </div>
  </div>

</template>

<script>

export default {
  name: 'main',
  data () {
    return {
      tmpNickname: ''
    }
  },
  methods: {
    goToLobby () {
      console.log(this.tmpNickname)
    }
    // 백엔드에 닉네임 중복인지 아닌지 요청보내기

  }
}
</script>

<style>

</style>
