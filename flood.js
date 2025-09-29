
import http from 'k6/http';
import { sleep } from 'k6';

export default function () {
  http.post('http://localhost:5000/data', JSON.stringify({ name: 'test', value: '123' }), {
    headers: { 'Content-Type': 'application/json' },
  });
  sleep(0.1); // Optional
}
