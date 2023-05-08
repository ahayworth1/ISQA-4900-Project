<template>
  <div class="container">
    <h2 class="title">Inventory</h2>
    <table class="table">
      <thead>
        <tr>
          <th>Name</th>
          <th> </th>
          <th>Description</th>
          <th>Quantity in Stock</th>
          <th>Price</th>
          <th> </th>
          
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in inventory" :key="index">
          <td>{{ item.name }}</td>
          <td><img :src="item.image" alt="image" style="max-width: 180px; max-height: 180px;"></td>
          <td>{{ item.description }}</td>
          <td>{{ item.quantity }}</td>
          <td>{{ '$' + item.price }}</td>
          <td>
            
            <button @click="addToCart(item)">Add to Cart</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import db from '@/boot/firebase.js'

export default {
  data() {
    return {
      inventory: [],
      cart: []
    }
  },
  created() {
    this.loadInventory()
    this.loadCart()
  },
  computed: {
    total() {
      return this.cart.reduce((total, item) => total + (item.quantity * item.price), 0)
    }
  },
  methods: {
    async loadInventory() {
      try {
        const querySnapshot = await db.collection('inventory').get()
        const inventory = []
        querySnapshot.forEach(doc => {
          inventory.push({
            id: doc.id,
            name: doc.data().name,
            description: doc.data().description,
            quantity: doc.data().quantity,
            price: doc.data().price,
            image: doc.data().image
          })
        })
        this.inventory = inventory
      } catch (error) {
        console.log(error)
      }
    },
    loadCart() {
  const cartString = localStorage.getItem('cart')
  if (cartString) {
    this.cart = JSON.parse(cartString)
  }
},

    async addToCart(item) {

      const inventoryItem = this.inventory.find(i => i.id === item.id)
      

      if (inventoryItem.quantity === 0) {
        console.log('Item is out of stock')
        return
      }
      

      const inventoryRef = db.collection('inventory').doc(item.id)
      await inventoryRef.update({
        quantity: item.quantity - 1
      })
      inventoryItem.quantity -= 1

      const existingCartItem = this.cart.find(cartItem => cartItem.id === item.id)
      if (existingCartItem) {
        existingCartItem.quantity += 1
      } else {
        const cartItem = {
          id: item.id,
          name: item.name,
          quantity: 1,
          price: item.price,
          image: item.image
        }
        this.cart.push(cartItem)
      }

      localStorage.setItem('cart', JSON.stringify(this.cart))

      this.$router.push('/cart')
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




