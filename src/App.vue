<template>
  <div class="bd">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/database">Database</router-link> |
      <router-link to="/files">Files</router-link> |
      <router-link to="/object">ObjectBasedStorage</router-link> |
      <router-link to="/images">Images</router-link> |
      <!--    <router-link to="/imageswiper">ImageSwiper</router-link> |-->
      <router-link to="/about">About</router-link>
    </nav>
    <div>
      <router-view />
    </div>
  </div>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: hsl(210, 14%, 56%);
  height: 100%;
  width: 100%;
}

nav {
  text-align: center;
  position: relative;
  width: 1200px;
  margin: 0 auto;
  padding: 20px;
  a {
    font-weight: bold;
    color: #131213;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

.bd {
  clear: both;
  min-width: 1200px;
  margin: 0;
  min-height: 675px;
}
</style>
