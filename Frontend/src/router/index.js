import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/Login.vue";

const routes = [
  {
    path: "/",
    redirect: "/login"
  },
  {
    path: "/login",
    component: Login
  },
  {
    path: "/dashboard",
    component: () => import("../views/Dashboard.vue")
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
