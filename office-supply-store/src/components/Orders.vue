<template>
   <div class="orders-container">
    <h1>Orders</h1>
    <ul>
      <li v-for="order in orders" :key="order.id">
      <div class="order-details"> 
        <div style="margin-right: 5px;"> Name: {{ order.firstName }} {{ order.lastName }},</div>
        <div style="margin-right: 5px;"> Email: {{ order.email }}, </div>
        <div style="margin-right: 5px;"> Shipping Address: {{ order.address }}, {{ order.city }}, {{ order.state }} {{ order.zipCode }}, </div>
        <div style="margin-right: 5px;"> Order ID: {{ order.id }}</div>
      </div>
      </li>
    </ul>
  </div>
</template>

<script>
import db from '@/boot/firebase.js'

export default {
  data() {
    return {
      orders: []
    }
  },
  created() {
    this.getOrders()
  },
  methods: {
    getOrders() {
      db.collection('orders').get()
        .then(querySnapshot => {
          let orders = []
          querySnapshot.forEach(doc => {
            orders.push({ id: doc.id, ...doc.data() })
          })
          this.orders = orders
        })
        .catch(error => {
          console.error('Error getting orders:', error)
        })
    }
  }
}
</script>


<style scoped>
.orders-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  list-style-type: none;
}

.order-list {
  list-style-type: none;
  padding: 0;
}

.order-details {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
  list-style-type: none;
}
</style>


