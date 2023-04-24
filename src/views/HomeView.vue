<!--<template>-->
<!--  <div class="home">-->
<!--    <img alt="Vue logo" src="../assets/logo.png" />-->
<!--    <HelloWorld msg="Welcome to Your Vue.js App" />-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--// @ is an alias to /src-->
<!--import HelloWorld from "@/components/HelloWorld.vue";-->

<!--export default {-->
<!--  name: "HomeView",-->
<!--  components: {-->
<!--    HelloWorld,-->
<!--  },-->
<!--};-->
<!--</script>-->

<template>
  <div class="bd">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/database">Database</router-link> |
      <router-link to="/files">Files</router-link> |
      <router-link to="/object">ObjectBasedStorage</router-link> |
      <router-link to="/about">About</router-link>
    </nav>
    <div class="home">
      <el-button type="primary">Whoami</el-button>
      <div>用户名: {{ user.userName }}</div>
      <div>姓名: {{ user.realName }}</div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";
export default {
  name: "MyHome",
  data() {
    return {
      user: {},
    };
  },
  created() {
    axios
      .post(
        "/api/user/info",
        {},
        {
          headers: {
            token: "666666",
          },
        }
      )
      .then((res) => {
        if (res.data.code === 0) {
          this.user = res.data.data;
        }
      });
  },
};
</script>

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
