<template>
  <div class="login-container">
    <form class="login-card" @submit.prevent="handleLogin">
      <h2>Login</h2>

      <input
        type="email"
        v-model="email"
        placeholder="Email"
        required
      />

      <input
        type="password"
        v-model="password"
        placeholder="Password"
        required
      />

      <button type="submit">Login</button>

      <p v-if="error" class="error">{{ error }}</p>
    </form>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      email: "",
      password: "",
      error: ""
    };
  },
  methods: {
    handleLogin() {
      if (!this.email || !this.password) {
        this.error = "All fields are required";
        return;
      }

      // TEMP: just checking dummy login
      if (this.email === "admin@test.com" && this.password === "1234") {
        alert("Login Successful");
        this.$router.push("/dashboard");
      } else {
        this.error = "Invalid credentials";
      }
    }
  }
};
</script>

<style scoped>
.login-container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #f4f6f8;
}

.login-card {
  width: 320px;
  padding: 30px;
  background: white;
  border-radius: 10px;
  box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}

input {
  width: 100%;
  padding: 10px;
  margin: 10px 0;
}

button {
  width: 100%;
  padding: 10px;
  background: #42b983;
  color: white;
  border: none;
  cursor: pointer;
}

.error {
  color: red;
  margin-top: 10px;
}
</style>
