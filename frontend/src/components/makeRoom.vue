<template>
  <div>
      <div><h3>make Room</h3></div>
      <div>
          <label for="">방 이름: </label>
          <input type="text" placeholder="방 제목" value='this.data'>
          <br>
          <label for=""> 인원수: </label>
          <input type="number" placeholder="인원 제한" value="5" min="0" max="100">
          <br>
          <label for="">판 수: </label>
          <input type="number" placeholder="몇판" value="6">
          <br>
          <label for="">비밀방?</label>
          <input type="checkbox" @click="togglePassword()">
          <br>
          <input type="password">
          <br>
          <button>방 만들기</button>
      </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      data: {
        name: '',
        number: ''
      },
      secret: false
    }
  },
  methods: {
    togglePassword () {
      this.secret = !this.secret
    }
  }
}
</script>

<style>

</style>
