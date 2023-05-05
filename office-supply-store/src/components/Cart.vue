<template>
    <div>
      <h1>Cart</h1>
      <table>
        <thead>
          <tr>
            <th>Item</th>
            <th>Price</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in cart" :key="item.id">
            <td>{{ item.name }}</td>
            <td>{{ item.price }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        cart: []
      }
    },
    mounted() {
      this.$root.$on('add-to-cart', this.addItemToCart);
    },
    beforeDestroy() {
      this.$root.$off('add-to-cart', this.addItemToCart);
    },
    methods: {
      addItemToCart(item) {
        this.cart.push(item);
        localStorage.setItem('cart', JSON.stringify(this.cart));
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
  
  
  
