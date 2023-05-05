<template>
    <div class="container">
      <h2 class="title">Checkout</h2>
      <form @submit.prevent="placeOrder">
        <div class="form-group">
          <label for="firstName">First Name:</label>
          <input type="text" id="firstName" v-model="firstName" required>
        </div>
        <div class="form-group">
          <label for="lastName">Last Name:</label>
          <input type="text" id="lastName" v-model="lastName" required>
        </div>
        <div class="form-group">
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="email" required>
        </div>
        <div class="form-group">
          <label for="address">Address:</label>
          <input type="text" id="address" v-model="address" required>
        </div>
        <div class="form-group">
          <label for="city">City:</label>
          <input type="text" id="city" v-model="city" required>
        </div>
        <div class="form-group">
          <label for="state">State:</label>
          <input type="text" id="state" v-model="state" required>
        </div>
        <div class="form-group">
          <label for="zipCode">Zip Code:</label>
          <input type="text" id="zipCode" v-model="zipCode" required>
        </div>
        <div class="form-group">
          <label for="cardInfo">Card Number:</label>
          <input type="text" id="cardInfo" v-model="cardInfo" required>
        </div>
        <div class="form-group">
          <label for="cardInfo">Card Expiration:</label>
          <input type="text" id="cardExp" v-model="cardExp" required>
        </div>
        <button type="submit">Place Order</button>
      </form>
      
    </div>
  </template>
  
  <script>
  import db from '@/boot/firebase.js'
  export default {
    data() {
      return {
        firstName: '',
        lastName: '',
        email: '',
        address: '',
        city: '',
        state: '',
        zipCode: '',
        cardInfo: '',
        cardExp: ''
      }
    },
    methods: {
      placeOrder() {
        // Save order data to Firebase or any other database of your choice
        const order = {
          firstName: this.firstName,
          lastName: this.lastName,
          email: this.email,
          address: this.address,
          city: this.city,
          state: this.state,
          zipCode: this.zipCode,
          cardInfo: this.cardInfo,
          cart: this.$parent.cart,
          total: this.$parent.total
        }
        db.collection('orders').add(order)
          .then(() => {
            // Show confirmation message and clear cart
            alert('Order placed successfully!')
            this.$parent.cart = []
            localStorage.removeItem('cart')
            this.$router.push('/')
          })
          .catch(error => {
            console.error('Error placing order:', error)
          })
      }
    }
  }
  </script>
 <style scoped>
 


 .form-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
  flex-wrap: nowrap;
  max-width: 150px;
}
.form {
    max-width: 500px;
}






</style>
