<template>
  <div class="login-container">
    <form class="login-card" @submit.prevent="handleLogin">
      <h2>Login</h2>

      <input type="email" v-model="email" placeholder="Email" required />
      <input type="password" v-model="password" placeholder="Password" required />

      <button type="submit">Login</button>

      <p v-if="error" class="error">{{ error }}</p>

      <p class="link" @click="$router.push('/register')">
        Don’t have an account? Register
      </p>
    </form>
  </div>
</template>

<script>
import api from "@/services/api";

export default {
  name: "Login",
  data() {
    return {
      email: "",
      password: "",
      error: "",
    };
  },
  methods: {
    async handleLogin() {
      this.error = "";

      try {
        const res = await api.post("/auth/login", {
          email: this.email,
          password: this.password,
        });

        localStorage.setItem("token", res.data.access_token);
        this.$router.push("/dashboard");

      } catch (err) {
        this.error =
          err.response?.data?.detail || "Login failed";
      }
    },
  },
};
</script>

<style scoped>
/* SAME CSS AS BEFORE */
.login-container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
.login-card {
  width: 320px;
  padding: 30px;
  background: white;
  border-radius: 10px;
}
.error {
  color: red;
}
.link {
  margin-top: 10px;
  cursor: pointer;
  color: #42b983;
}
</style>
