import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/components/Home.vue'
import Auth from '@/components/Auth.vue'
import Inventory from '@/components/Inventory.vue'
import Register from '@/components/Register.vue'
import Orders from '@/components/Orders.vue'
import Cart from '@/components/Cart.vue'
import Checkout from '@/components/Checkout.vue'
import Logout from '@/components/Logout.vue'
import OrderConfirmation from '@/components/OrderConfirmation.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/inventory',
    name: 'Inventory',
    component: Inventory,
  },
  {
    path: '/auth',
    name: 'Auth',
    component: Auth
  },
   {
     path:'/register',
     name: 'Register',
     component: Register
   },
  {
     path:'/orders',
     name: 'Orders',
     component: Orders
   },
   {
    path:'/cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/checkout',
    name: 'Checkout',
    component: Checkout
  },
  {
    path: '/logout',
    name: 'Logout',
    component: Logout
  },
  {
    path: '/orderconfirmation',
    name: 'OrderConfirmation',
    component: OrderConfirmation
  },
]
  const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
  })
  
  export default router
