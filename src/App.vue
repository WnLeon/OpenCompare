<template>
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
  <nav>
    <footer class="footer">
      <p>&copy; 2023 MyWebsite. All Rights Reserved.</p>
      <div class="social-links">
        <a href="#"><i>QQ</i></a>
        <a href="#"><i>WECHAT</i></a>
        <a href="#"><i>FACEBOOK</i></a>
      </div>
    </footer>
  </nav>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: hsl(210, 22%, 93%);
  height: 100%;
  width: 100%;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #131213;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

.footer {
  text-align: center;
  width: 100%;
  bottom: 0;
  background-color: hsl(90, 2%, 25%);
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
}

.social-links a {
  margin-right: 0.5rem;
  color: hsl(0, 14%, 90%);
  transition: color 0.3s ease;
}

.social-links a:hover {
  color: hsl(0, 14%, 90%);
}
</style>
