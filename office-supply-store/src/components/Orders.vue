<template>
  <div>
    <h1 class="title">Order List</h1>
    <ul>
      <li v-for="(order, index) in orders" :key="index">
        {{ order.orderName }} - Quantity: {{ order.quantity }} - Price: {{ order.price }}
        <!-- <img v-if="order.orderName === 'Pencils'" :src="require(`@/assets/OfficePencil1.jpg`)" alt="Pencil Image" height="100" />
        <img v-if="order.orderName === 'Chair'" :src="require(`@/assets/OfficeChair1.jpg`)" alt="Chair Image" height="100" />
        <img v-if="order.orderName === 'Pens'" :src="require(`@/assets/OfficePen1.jpg`)" alt="Pen Image" height="100" />
        <img v-if="order.orderName === 'Desk'" :src="require(`@/assets/OfficeDesk1.jpg`)" alt="Desk Image" height="100" /> -->
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Orders',
  data() {
    return {
      orders: [
        { orderName: 'Pencils', quantity: 2, price: 1 },
        { orderName: 'Chair', quantity: 1, price: 50 },
        { orderName: 'Pens', quantity: 3, price: 2 },
        { orderName: 'Desk', quantity: 1, price: 100 }
      ]
    }
  }
}
</script>

<style>
.title {
  font-size: 2em;
  text-align: center;
  margin-bottom: 1em;
}
ul {
  text-align: center;
  font-size: 20px;
  padding: 0;
  list-style: none; /* remove bullets */
}
li {
  margin-bottom: 0.5em;
}
</style>
