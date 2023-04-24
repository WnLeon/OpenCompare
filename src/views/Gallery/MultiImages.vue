<!-- MultiImages.vue -->
<template>
  <nav>
    <router-link to="/images/scenery">Scenery</router-link> |
    <router-link to="/images/laughing">Laughing</router-link> |
    <router-link to="/images/beauty">Beauty</router-link> |
    <router-link to="/images/animal">Animal</router-link> |
    <router-link to="/images/innovation">Innovation</router-link>
  </nav>
</template>

<style lang="scss">
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
</style>
