import axios from 'axios';


const protocol = 'http'; 
const host = process.env.VUE_APP_API_HOST;
const port = process.env.VUE_APP_API_PORT;
const baseURL = `${protocol}://${host}:${port}`;

const apiClient = axios.create({
  baseURL: baseURL,
  headers: {
    'Content-Type': 'application/json'
  }
});

export default apiClient;