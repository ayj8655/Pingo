<template>
  <div>
    <div>
        <canvas id="jsCanvas" class="canvas" width="700" height="700" ref="canvas" @mousemove="onMouseMove" @mousedown="onMouseDown" @mouseup="onMouseUp" @mouseleave="stopPainting"></canvas>
    </div>
    <div class="controls__range">
        <input type="range" id="jsRange" v-model="data.jsRange" min="0.1" max="5" step="0.1">
    </div>
    <div class='controls__btns'>
        <button id='jsMode' @click="eraseAll">Erase All</button>
        <button id='jsSave' @click="sendImage">Save</button>
    </div>
    <div class='controls'>
        <div class='controls__colors' id="jsColors">
            <div class="controls__color" @click="setColor(0)" style="background-color: black"></div>
            <div class="controls__color" @click="setColor(1)" style="background-color: white"></div>
            <div class="controls__color" @click="setColor(2)" style="background-color: #ff3b3c"></div>
            <div class="controls__color" @click="setColor(3)" style="background-color: #ff9500"></div>
            <div class="controls__color" @click="setColor(4)" style="background-color: #ffcc00"></div>
            <div class="controls__color" @click="setColor(5)" style="background-color: #4cd963"></div>
            <div class="controls__color" @click="setColor(6)" style="background-color: #5ac8fa"></div>
            <div class="controls__color" @click="setColor(7)" style="background-color: #0579ff"></div>
            <div class="controls__color" @click="setColor(8)" style="background-color: #5856d6"></div>
        </div>
    </div>

</div>
</template>

<script>
import { ref, reactive, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

export default {
  setup () {
    const canvas = ref()
    const router = useRouter()

    const data = reactive({
      painting: false,
      erasing: false,
      ctx: 0,
      colors: {
        0: 'black',
        1: 'white',
        2: '#ff3b3c',
        3: '#ff9500',
        4: '#ffcc00',
        5: '#4cd963',
        6: '#5ac8fa',
        7: '#0579ff',
        8: '#5856d6'
      },
      jsRange: 2.5
    })

    onMounted(() => {
      prepare()
      console.log('prepare')
    })

    const prepare = () => {
      console.log(canvas.value)
      data.ctx = canvas.value.getContext('2d')
      //   console.log(data.ctx)
      canvas.value.fillStyle = 'white'
      // canvas.value.fillRect(0, 0, 700, 700)
      data.ctx.strokeStyle = '#2c2c2c'
      data.ctx.lineWidth = data.jsRange

      console.log(data.ctx)
    }

    const startPainting = () => {
      data.paiting = true
    }

    const stopPainting = () => {
      data.painting = false
    }

    const onMouseMove = (event) => {
    //   console.log(event)
    //   prepare()
      const x = event.offsetX
      const y = event.offsetY
      // console.log(x, y)

      if (!data.painting) {
        data.ctx.beginPath()
        data.ctx.moveTo(x, y)
      } else {
        data.ctx.lineTo(x, y)
        data.ctx.stroke()
      }
    }

    const onMouseDown = (event) => {
      data.painting = true
    //   console.log(canRef.value)
    }

    const onMouseUp = (event) => {
      stopPainting()
    }

    const setColor = (num) => {
      data.ctx.strokeStyle = data.colors[num]
    }

    const handleRangeChange = (event) => {
      console.log(event)
    }

    

    const sendImage = () => {
      canvas.value.toBlob(function (blob) {
        const formData = new FormData()
        // 이부분에 접속한 유저, 들어온 방, 정해진 category 를 지정해줘야 함
        formData.append('user', 1)
        formData.append('room', 1)
        formData.append('category', 1)
        formData.append('image', blob, 'filename.png')
        axios.post(
          'http://127.0.0.1:8000/paint_game/saving/',
          formData,
          { headers: { 'Content-Type': 'multipart/form-data' } }
        )
          .then(res => {
            console.log(res)
            router.push('/play/score')
            console.log('성공')
          })
          .catch(err => {
            console.log(err)
          })
      })
    }

    // 임시 방편인데 새로고침 말고 더 좋은 방법 없으려나...
    const eraseAll = () => {
      data.ctx.clearRect(0, 0, 700, 700)
    }

    const erase = () => {

    }
    // 붓 사이즈 조절하는거 아직 못함
    return {
      startPainting,
      stopPainting,
      onMouseMove,
      onMouseDown,
      onMouseUp,
      prepare,
      setColor,
      handleRangeChange,
      sendImage,
      eraseAll,
      erase,
      data,
      canvas,
      router
    }
  }
}
</script>

<style>
body {
    background-color: #f6f9fc;
    font-family: -apple-system, -apple-system, BlinkMacSystemFont,
    'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell,
    'Open Sans', 'Helvetica Neue', sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 50px 0px;
}

.canvas {
    width: 700px;
    height: 700px;
    background-color: white;
    border-radius: 15px;
    box-shadow: 0 4px 6px rgba(50, 50, 93, 0.11), 0, 1px 3px rgba(0, 0, 0, 0.08);
}

.controls {
    margin-top: flex;
}

.controls .controls__btns{
    margin-bottom: 30px;
}

.controls__btns button {
    all: unset;
    cursor: pointer;
    background-color: white;
    padding: 5px 0px;
    width: 80px;
    text-align: center;
    border-radius: 5px;
    box-shadow: 0 4px 6px rgba(50, 50, 93, 0.11), 0 1px 3px rgba(0,0,0,0.08);
    border: 2px solid rgba(0, 0, 0, 0.2);
    color: rgba(0, 0, 0, 0.7);
    text-transform: uppercase;
    font-weight: 800;
    font-size: 12px;
}
.controls__btns button:active{
    transform: scale(0.98)
}

.controls .controls__colors{
    display: flex;
}

.controls__colors .controls__color{
    width: 50px;
    height: 50px;
    border-radius: 25px;
    cursor: pointer;
    box-shadow: 0 4px 6px rgba(50, 50, 93, 0.11), 0 1px 3px rgba(0, 0, 0, 0.08);
}
</style>
