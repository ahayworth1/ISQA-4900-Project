<template>
  <div>
    <h2>Register</h2>
    <form @submit.prevent="register">
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required>
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required>
      </div>
      <div>
        <button type="submit">Register</button>
      </div>
    </form>
  </div>
</template>

<script>
import firebase from 'firebase/app';
import 'firebase/auth';
export default {
  data() {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    register() {
      const auth = firebase.auth();
      auth.createUserWithEmailAndPassword(this.email, this.password)
        .then(userCredential => {
          console.log(userCredential)
          this.$router.push('/');
        })
        .catch(error => {
          console.error(error)
        })
    }
  }
}
</script>


