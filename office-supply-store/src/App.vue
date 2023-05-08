<template>
    <ul class="nav justify-content-end">
      <div class="EFS">The Office, Office Supply Store</div>
      <li class="nav-item active">
        <router-link to="/">Home</router-link> 
      </li>
      <li class="nav-item">
        <router-link to="/inventory">Inventory</router-link>
      </li>
      <template v-if="authenticated">
        <li class="nav-item">
          <router-link to="/cart">Cart</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/orders">Orders</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/logout" @click.prevent="logout">Log Out</router-link>
        </li>
      </template>
      <template v-else>
        <li class="nav-item">
          <router-link to="/auth">Login</router-link>
        </li> 
        <li class="nav-item">
          <router-link to="/register">Register</router-link>
        </li>
      </template>
    </ul> 
    <router-view/>
  </template> 
  <script>
  import firebase from 'firebase/app';
  import 'firebase/auth';
  
  export default {
    name: 'App',
    data() {
      return {
        authenticated: false,
      };
    },
    mounted() {
      firebase.auth().onAuthStateChanged((user) => {
        if (user) {
          this.authenticated = true;
        } else {
          this.authenticated = false;
        }
      });
    },
    methods: {
      logout() {
        firebase.auth().signOut().then(() => {
          this.authenticated = false;
          this.$router.push('/');
        }).catch((error) => {
          console.log(error.message);
        });
      },
    },
  };
  </script>


  


<style lang="scss">
  #app {
      font-family: Avenir, Helvetica, Arial, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-align: center;
      color: #2c3e50;
  }
  #nav {
      padding: 30px;
      background-color: cadetblue;
      
      
      a {
          font-weight: bold;
          color: #2c3e50;
          &.router-link-exact-active {
              color: #42b983;
          }
      }
  }
  .nav {
      padding: 1em;
      background-color: cadetblue;
      width: 1400px;
      
      li {
  display: inline-block;
  vertical-align: top;
  font-weight: bold;
  color: #2c3e50;
  list-style: none;
}



      a {
          color: black;
          padding: .5em;


          &.router-link-exact-active {
              color: #42b983;
          }
      }


      .EFS{
          text-align: center;
          font-weight: bold;
          font-size: 30px;

      }
  }


</style> -->


