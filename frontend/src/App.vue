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
  min-height: 100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(to right, #3883BC 0%, 50%, #FFF9BA 100%);

}
/* Gradient in Hex */
/* linear-gradient(to right, #3883BC 0%, 50%, #FFF9BA 100%); */

/* Gradient in RGBA */
/* linear-gradient(to right, rgba(56, 131, 188, 1) 0%, 50%, rgba(255, 249, 186, 1) 100%); */
</style>
