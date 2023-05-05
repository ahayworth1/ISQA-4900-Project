
   <template>
    <div>
      <h2>Login</h2>
      <form>
        <label>Email:</label>
        <input type="email" v-model="email">
        <br><br>
        <label>Password:</label>
        <input type="password" v-model="password">
        <br><br>
        <button @click.prevent="login">Login</button>
      </form>
      <p v-if="errorMessage">{{ errorMessage }}</p>
    </div>
  </template>
  
  <script>
  import firebase from 'firebase/app';
  import 'firebase/auth';
  
  export default {
    data() {
      return {
        email: '',
        password: '',
      };
    },
    methods: {
    async login() {
      try {
        await firebase.auth().signInWithEmailAndPassword(this.email, this.password);
        console.log('Logged in successfully');
        this.$router.push('/');
      } catch (error) {
        if (error.code === 'auth/user-not-found' || error.code === 'auth/wrong-password') {
          this.errorMessage = 'Incorrect email or password.';
        }
      }
    },
  },
};
</script>