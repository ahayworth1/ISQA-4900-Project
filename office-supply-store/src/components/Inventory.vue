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
      inventory: []
    }
  },
  created() {
    this.loadInventory()
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
    async addToCart(item) {
  // Decrement the quantity of the item in the inventory
  const inventoryRef = db.collection('inventory').doc(item.id)
  await inventoryRef.update({
    quantity: item.quantity - 1
  })
  item.quantity -= 1

  // Add the item to the cart
  this.cart.push(item);

  // Store the updated cart in localStorage
  localStorage.setItem('cart', JSON.stringify(this.cart));

  // Redirect to the cart page
  this.$router.push('/cart');
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




