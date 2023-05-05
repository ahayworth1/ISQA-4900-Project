<template>
  <div class="container">
    <h2 class="title">Cart</h2>
    <table class="table">
      <thead>
        <tr>
          <th>Item</th>
          <th> </th>
          <th>Quantity</th>
          <th>Price</th>
          <th>Total</th>
          <th> </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in cart" :key="index">
          <td>{{ item.name }}</td>
          <td><img :src="item.image" alt="image" style="max-width: 180px; max-height: 180px;"></td>
          <td>
            <div class="input-group">
              <input type="number" min="1" :max="item.stock" v-model="item.quantity" @input="updateCart(item)">
              <!-- <span v-if="item.quantityToAdd">{{ item.quantityToAdd }}</span> -->
            </div>
          </td>
          <td>{{ '$' + item.price }}</td>
          <td>{{ '$' + (item.quantity * item.price) }}</td>
          <td>
            <button @click="removeFromCart(item)">Remove</button>
          </td>
        </tr>
      </tbody>
    </table>
    <div class="total">
      Total: {{ '$' + total }}
    </div>
    <button @click="navigateToCheckout"> Checkout</button>

  </div>
</template>

<script>
import db from '@/boot/firebase.js'
export default {
  // props: {
  //   quantityToAdd: {
  //     type: Number,
  //     default: 0
  //   }
  // },
  data() {
    return {
      cart: []
    }
  },
  created() {
    this.loadCart()
  },
  computed: {
    total() {
      return this.cart.reduce((total, item) => total + (item.quantity * item.price), 0)
    }
  },
  methods: {
    navigateToCheckout() {
      this.$router.push('/checkout')
    },
    loadCart() {
      const cart = JSON.parse(localStorage.getItem('cart')) || []
      this.cart = cart
     
    },
    removeFromCart(item) {
      const index = this.cart.findIndex(cartItem => cartItem.id === item.id)
      if (index > -1) {
        this.cart.splice(index, 1)
      }
      this.updateCart(item)
    },
    updateCart(item) {
      // Update the item's quantity in the cart
      const cartItem = this.cart.find(cartItem => cartItem.id === item.id)
      if (cartItem) {
        cartItem.quantity = item.quantity
      }

      // Update the item's stock in the inventory
      const inventoryRef = db.collection('inventory').doc(item.id)
      if (typeof item.stock === 'number' && typeof item.quantity === 'number') {
        inventoryRef.update({
          quantity: item.stock - item.quantity
        })
      }

      // Store the updated cart in localStorage
      localStorage.setItem('cart', JSON.stringify(this.cart))
    }
  }

}

</script>






  
  <style scoped>
.container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 20px;
}

.title {
  font-size: 30px;
  margin-bottom: 20px;
}

.table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
}

th,
td {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #ddd;
  font-size: 20px;
}

th {
  background-color: #f2f2f2;
  font-weight: bold;
  font-size: 20px;
}
</style>
  
  
  
