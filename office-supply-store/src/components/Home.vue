<template>
  <!-- Welcome Text -->
  <div class="container-fluid">
    <div class="row">
      <div class="col col-12 align-items-center justify-content-center">
      </div>
    </div>
  </div>
  <div class="d-flex justify-content-center mb-4">
  <img :src="require('@/assets/office.gif')" class="card-img-top" style="height: 15rem; margin-bottom: 2rem;">
</div>
        <blockquote>
          &ldquo;Welcome {{ validUserName }}!&rdquo;
          <footer>
            <small>
              <em>&mdash;The Office, Office Supply Store.</em>
            </small>
          </footer>
        </blockquote>
  <div class="container-fluid">
  <div class="row align-items-center justify-content-center">
    <div class="col col-12 col-sm-10 col-md-10">
      <div class="card-deck">
        <div class="card border-secondary mb-3" style="max-width: 18rem;">
          <img :src="require('@/assets/cart.png')" class="card-img-top" style="height: 15rem">
          <div class="card-body">
            
            <button class="btn btn-outline-secondary" @click="$router.push('/cart')">View Your Cart</button>
          </div>
        </div>
        <div class="card border-secondary mb-3" style="max-width: 18rem;">
          <img :src="require('@/assets/inventory.png')" class="card-img-top" style="height: 15rem">
          <div class="card-body">
            
            <button class="btn btn-outline-secondary" @click="$router.push('/inventory')">View Our Inventory</button>
          </div>
        </div>
        <div class="card border-secondary mb-3" style="max-width: 18rem;">
          <img :src="require('@/assets/orders.png')" class="card-img-top" style="height: 15rem">
          <div class="card-body">
            
            <button class="btn btn-outline-secondary" @click="$router.push('/orders')">View Your Orders</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>




</template>
<style> 
div {
  display: inline-block;
vertical-align: top;
font-weight: bold;
color: #2c3e50;
list-style: none;}
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

