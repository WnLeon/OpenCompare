import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import VueFlexbox from "vue-flexbox";

createApp(App)
  .use(store)
  .use(router)
  .use(ElementPlus)
  .use(VueFlexbox)
  .mount("#app");
