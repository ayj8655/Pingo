<template >
  <div class="ai-back" >
    <button id="yellow-button" @click="start" v-if="!isStarted">start</button>
    <div class="word-box">
      <div class="word" v-if="isStarted">
        <p>제시어</p>
      </div>
    </div>

    <div :class="['chat-only', isStarted && 'chat-and-draw']" >
      <!-- 그림판 -->
      <div class="draw" v-if="isStarted">
        <draw/>
      </div>
      <div :class="['big-chat', isStarted && 'chat']" >
        <chating />
      </div>
    </div>

  </div>
  <!-- 시작버튼(누르면 없어지고 제시어 등장) -->

</template>

<script>
import { onMounted, ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";
import draw from "../components/room/draw.vue"
import chating from "../components/room/chating.vue"
export default {
  components: { draw, chating },
  setup() {
    // const start(() => {
    //   // const router = userRouter()
    //   console.log(this.$route.params);
    //   const room_id = this.$route.params;
    //   localStorage.setItem("room_id", room_id.room_id);
    //   console.log(room_id.room_id);
    //   this.$router.push({ name: "play", params: { room_id: room_id.room_id } });
    // },)
    const isStarted = ref(false)
    const start = () => {
      isStarted.value = !isStarted.value
    }

    return {
      start,
      isStarted
    }
}
}
</script>

<style>
.ai-back{
  /* background-image: url(/image1.jfif) !important ; */
  background-image: url(/ai.jpg) !important ;
  height: 960px;
  background-repeat : repeat;
  background-size : cover;
  background-position: center;
}

.chat-only{
  display: block;

}
.chat-and-draw{
  display: flex;
  justify-content: center;
  flex-direction: row;
}
.draw{
  height: 800px;
  width: 800px;
  padding: auto;
  /* flex-grow: 2; */
  /* 캔버스 크기가 고정되어 안커짐 */


}
.big-chat{
  height: 800px;
  width: 500px;
  background-color: #fff;
  border-radius: 15px;
  margin: auto;
}
.chat{
  height: 600px;
  width: 300px;
  background-color: #fff;
  border-radius: 15px;
  margin: 0;
  /* flex-grow: 1; */
}
.word-box{
  display: flex;
  justify-content: center;
}
.word{
  height: 3rem;
  width: 18rem;
  border-radius: 0.5rem;
  border: none;
  font-size: 1.3rem;
  background: #FFF9BA;
  color: #3883BC;
  font-weight: bold;
  margin: 10px;
  align-content: center;
}

.word p {
  font-size: 1.4rem !important;
  margin: 0.6rem;
}
</style>
