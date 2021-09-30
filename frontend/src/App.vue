<template >
  <div id="back">
    <div id="nav">
      <!-- <router-link to="/login">login</router-link> -->

    </div>
    <router-view/>
  </div>

</template>

<style>


#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  min-height: 100% ;
  width: 100%;
  height: 100vh;
  background-image: '../public/gradient.png';
  background: linear-gradient(to right, #3883BC 0%, 50%, #FFF9BA 100%);
  background-size: cover !important;
  padding: 0 !important;
  margin: 0 !important;
}

#nav {

}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

#back {
  min-height: 70%;
  width: 100%;
  height: 100%;
  background: linear-gradient(to right, #3883BC 0%, 50%, #FFF9BA 100%);

}

/* 공통사용 버튼 */
#blue-button {
  height: 3rem;
  width: 18rem;
  border-radius: 0.5rem;
  border: none;
  font-size: 1.3rem;
  background: #3883BC;
  color: white;
  font-weight: bold;
  margin: 10px;
}

#blue-button:hover {
  /* height: 3.3rem;
  width: 18.5rem; */
  transition: 0.1s;
  background-color: #FFF9BA;
  /* box-shadow: 0 0 0 1px #1a3d58 inset; */
  cursor: pointer;
  color: #3883BC;


}

#yellow-button {
  height: 3rem;
  width: 18rem;
  border-radius: 0.5rem;
  border: none;
  font-size: 1.3rem;
  background: #FFF9BA;
  color: #3883BC;
  font-weight: bold;
  margin: 10px;
}

#yellow-button:hover {
  /* height: 3.3rem;
  width: 18.5rem; */
  transition: 0.1s;
  background-color: white;
  /* box-shadow: 0 0 0 1px #1a3d58 inset; */
  cursor: pointer;
  color: #3883BC;
  font-size: 1.5rem;


}
/* Gradient in Hex */
/* linear-gradient(to right, #3883BC 0%, 50%, #FFF9BA 100%); */

/* Gradient in RGBA */
/* linear-gradient(to right, rgba(56, 131, 188, 1) 0%, 50%, rgba(255, 249, 186, 1) 100%); */
</style>
