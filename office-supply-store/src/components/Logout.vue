<template>
    <div>
      <h1>Log Out</h1>
      <button @click="logout">Log Out</button>
    </div>
  </template>
  
  <script>
  import firebase from 'firebase/app';
  import 'firebase/auth';
  
  export default {
    methods: {
      logout() {
        firebase.auth().signOut().then(() => {
          console.log('Logged out successfully');
          this.$router.push('/auth');
        }).catch((error) => {
          console.error(error);
        });
      },
    },
  };
  </script>
  