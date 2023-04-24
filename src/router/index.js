import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/database",
    name: "database",
    component: () =>
      import(/* webpackChunkName: "database" */ "../views/DatabaseView.vue"),
  },
  {
    path: "/files",
    name: "files",
    component: () =>
      import(/* webpackChunkName: "files" */ "../views/FilesView.vue"),
  },
  {
    path: "/object",
    name: "object",
    component: () =>
      import(/* webpackChunkName: "object" */ "../views/ObjectStorageView.vue"),
  },
  {
    path: "/images",
    name: "images",
    component: () =>
      import(/* webpackChunkName: "object" */ "../views/Gallery/myBeauty.vue"),
  },
  {
    path: "/images/beauty",
    name: "beauty",
    component: () =>
      import(/* webpackChunkName: "object" */ "../views/Gallery/myBeauty.vue"),
  },
  {
    path: "/images/animal",
    name: "animal",
    component: () =>
      import(/* webpackChunkName: "object" */ "../views/Gallery/myAnimal.vue"),
  },
  {
    path: "/images/scenery",
    name: "scenery",
    component: () =>
      import(/* webpackChunkName: "object" */ "../views/Gallery/myScenery.vue"),
  },
  {
    path: "/images/laughing",
    name: "laughing",
    component: () =>
      import(
        /* webpackChunkName: "object" */ "../views/Gallery/myLaughing.vue"
      ),
  },
  {
    path: "/images/innovation",
    name: "innovation",
    component: () =>
      import(
        /* webpackChunkName: "object" */ "../views/Gallery/myInnovation.vue"
      ),
  },
  {
    path: "/login",
    name: "login",
    component: () =>
      import(/* webpackChunkName: "object" */ "../components/Login.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
