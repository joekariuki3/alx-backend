import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
	  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
	  console.error(`Redis client not connected to the server: ${err}`);
});
function setData(key, data) {
  for (let field of Object.keys(data)) {
    client.hset(key, field, data[field], redis.print);
  }
}
function displayData(key) {
  client.hgetall(key, (error, result) => {
  console.log(result);
  })
}
const key = 'HolbertonSchools'
const data = {"Portland": 50, "Seattle": 80, "New York": 20, "Bogota": 20, "Cali": 40, "Paris": 2}
setData(key, data);
displayData(key);
