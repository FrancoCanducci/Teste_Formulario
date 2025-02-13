import http from 'k6/http';
import { check, sleep } from 'k6';
import { Trend, Rate } from 'k6/metrics';

// Métricas customizadas
let responseTime = new Trend('response_time');
let errorRate = new Rate('error_rate');

export let options = {
  vus: 100, // Número de usuários simultâneos
  duration: '30s', // Duração do teste
};

export default function () {
  let res = http.get('https://jsonplaceholder.typicode.com/posts/1'); // Testando um endpoint válido

  // Registrar tempo de resposta
  responseTime.add(res.timings.duration);
  
  // Verificar se a resposta está dentro do esperado
  let success = check(res, {
    'status code is 200': (r) => r.status === 200,
    'response body is not empty': (r) => r.body.length > 0,
  });
  
  // Registrar taxa de erro
  errorRate.add(res.status !== 200);
  
  sleep(1); // Espera entre requisições
}
