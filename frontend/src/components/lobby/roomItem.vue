<template>
  <div>
    <head>
      <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.4/css/all.css" integrity="sha384-DyZ88mC6Up2uqS4h/KRgHuoeGwBcD4Ng9SiP4dIRy0EXTlnuz47vAwmeGwVChigm" crossorigin="anonymous">
    </head>
    <div class="room-box">
      <div class="room-box-left">
        <!-- <p>{{room.room_id}} 번방</p> -->
        <p>방이름: {{room.room_name}} </p>
        <p>방장:{{room.room_owner}}</p>
        <p>문제수: {{room.problems}}</p>
      </div>

      <div class="room-box-right">
        <i :class="['fas fa-pen', !room.is_started && 'state']"  ></i>
        <i :class="['fas fa-lock', !room.is_locked && 'state']" ></i>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: 'roomItem',
  props: {
    room: {
      type: Object
    }
  },
  emit: {
  }
}
</script>

<style>
  .room-box {
    display: flex;
    justify-content:left;
    width: 18rem;
    height: 5rem;
    background-color: #FFF9BA;
    margin: 10px;
    box-shadow: 2px 2px 6px 0 #94906b;
    cursor: pointer;
    padding: 0.1rem;
    align-items: center;
    justify-content: space-between;
    flex-basis: 40%;
  }
  .room-box:hover {
    display: flex;
    justify-content: left;
    width: 18.1rem;
    height: 5rem;
    background-color: #FFF9BA;
    margin: 10px;
    box-shadow: 2px 2px 6px 0 #94906b;
    cursor: pointer;
    justify-content: space-between;
  }
  .room-box-left{
    display: flex;
    justify-content: left;
    margin-left: 1rem;
    flex-direction: column;
    justify-items: start;
  }
  .room-box-left p {
    margin: 0;
    font-size: 0.8rem;
  }
  .room-box-right{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    margin-right: 1rem;
  }
  .state{
    color: #cecece;
    margin-top: 0.5rem;
    margin-bottom: 0.5rem;
  }
</style>
