<template>
  <div class="bd">
    <router-view />
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
.bd {
  clear: both;
  min-width: 1200px;
  margin: 0;
  min-height: 675px;
}
</style>
