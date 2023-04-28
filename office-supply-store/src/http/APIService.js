import axios from 'axios';
const API_URL = 'https://ahayworth20.pythonanywhere.com/'; /* 'http://localhost:8000' http://127.0.0.1:8000/ or  'https://movies-groyce.pythonanywhere.com/'*/

export class APIService {
  constructor() {

  }



  authenticateLogin(credentials) {
    const url = `${API_URL}/auth/`;
    return axios.post(url, credentials);
  }

  registerUser(credentials) {
     const url = `${API_URL}/register/`;
     credentials.customusername = credentials.username
     return axios.post(url, credentials);
  }
}
