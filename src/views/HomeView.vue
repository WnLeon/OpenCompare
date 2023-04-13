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
  <div class="home">
    <el-button type="primary">Whoami</el-button>
    <div>用户名: {{ user.userName }}</div>
    <div>姓名: {{ user.realName }}</div>
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
