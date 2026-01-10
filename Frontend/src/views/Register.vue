<template>
  <div class="login-container">
    <form class="login-card" @submit.prevent="handleRegister">
      <h2>Register</h2>

      <input type="email" v-model="email" placeholder="Email" required />
      <input type="password" v-model="password" placeholder="Password" required />

      <button type="submit">Register</button>

      <p v-if="error" class="error">{{ error }}</p>

      <p class="link" @click="$router.push('/login')">
        Already have an account? Login
      </p>
    </form>
  </div>
</template>

<script>
import api from "@/services/api";

export default {
  name: "Register",
  data() {
    return {
      email: "",
      password: "",
      error: "",
    };
  },
  methods: {
    async handleRegister() {
      this.error = "";

      try {
        await api.post("/auth/register", {
          email: this.email,
          password: this.password,
        });

        alert("Registration successful!");
        this.$router.push("/login");

      } catch (err) {
        this.error =
          err.response?.data?.detail || "Registration failed";
      }
    },
  },
};
</script>

<style scoped>
/* reuse same styles */
</style>
