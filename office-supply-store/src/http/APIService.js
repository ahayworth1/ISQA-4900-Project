import axios from 'axios';

const API_URL = 'http://callahanpilkington.pythonanywhere.com';

export class APIService {
  constructor() {}

  getInventory() {
    const url = `${API_URL}/api/inventory/`;
    return axios.get(url);
  }

  authenticateLogin(credentials) {
    const url = `${API_URL}/auth/`;
    return axios.post(url, credentials);
  }

  registerUser(credentials) {
    const url = `${API_URL}/register/`;
    credentials.customusername = credentials.username;
    return axios.post(url, credentials);
  }
}
