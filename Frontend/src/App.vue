<template>
  <div class="container">
    <h1>Demo API Data</h1>

    <button @click="fetchDemo">Fetch Data</button>

    <table v-if="apiData" border="2" cellpadding="8">
      <thead>
        <tr>
          <th>Key</th>
          <th>Value</th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td>Status</td>
          <td>{{ apiData.status }}</td>
        </tr>
        <tr>
          <td>Message</td>
          <td>{{ apiData.message }}</td>
        </tr>
        <tr>
          <td>App Name</td>
          <td>{{ apiData.data.app }}</td>
        </tr>
        <tr>
          <td>Version</td>
          <td>{{ apiData.data.version }}</td>
        </tr>
        <tr>
          <td>Features</td>
          <td>
            <ul>
              <li v-for="(feature, index) in apiData.data.features" :key="index">
                {{ feature }}
              </li>
            </ul>
          </td>
        </tr>
      </tbody>
    </table>

<h2>{{ apiData.data.features }}</h2>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref } from "vue"

const apiData = ref(null)
const error = ref(null)

const fetchDemo = async () => {
  try {
    const res = await fetch("http://127.0.0.1:8000/demo")
    if (!res.ok) throw new Error("API request failed")

    apiData.value = await res.json()
  } catch (err) {
    error.value = err.message
  }
}
</script>

<style>
.container {
  padding: 20px;
}
table {
  margin-top: 20px;
  border-collapse: collapse;
  width: 60%;
}
th {
  background: #f4f4f4;
}
.error {
  color: red;
}
</style>
