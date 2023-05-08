<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col col-12 align-items-center justify-content-center">
      </div>
    </div>
  </div>
  <div class="d-flex justify-content-center mb-4">
  <img :src="require('@/assets/office.gif')" class="card-img-top" style="height: 15rem; margin-bottom: 0px;">
</div>
        <blockquote>
          Welcome to our store! Please <button class="btn btn-outline-secondary" @click="$router.push('/auth')">Login</button>or <button class="btn btn-outline-secondary" @click="$router.push('/register')">Register</button> to continue.
          <footer>
            <small>
              <em>&mdash;The Office, Office Supply Store.</em>
            </small>
          </footer>
        </blockquote>
</template>
<style> 
div {
  display: inline-block;
vertical-align: top;
font-weight: bold;
color: #2c3e50;
list-style: none;};

</style>


<script>
import router from '../router'

export default {
  name: 'Home',
  data() {
    return {
      validUserName: 'Guest'
    }
  },
  mounted() {
    this.getUser()
  },
  methods: {
    getUser() {
      if (localStorage.getItem('isAuthenticated') && JSON.parse(localStorage.getItem('isAuthenticated')) === true) {
        this.validUserName = JSON.parse(localStorage.getItem('log_user'))
      }
    }
  }
}
</script>


