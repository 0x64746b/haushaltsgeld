import { fetchExpense } from './client-db';

const CACHE = 'haushaltsgeld';

self.addEventListener('install', function(event) {
  console.log('The service worker is being installed.');
  event.waitUntil(cacheAppShell());
});

self.addEventListener('fetch', function(event) {
  console.log('The service worker is serving the asset.');
  event.respondWith(fromNetwork(event.request, 400).catch(function () {
    return fromCache(event.request);
  }));
});

self.addEventListener('sync', function(event) {
  console.log('Preparing to sync...');
  let [eventType, expenseId] = event.tag.split(/-(.+)/);
  if (eventType === 'expenseStored') {
    console.log(` Processing request to sync expense '${expenseId}'`);
    fetchExpense(expenseId).then(function(expense) {
      console.log(` Retrieved expense ${expense.expenseId}`);
    });
  }
});

function cacheAppShell() {
  return caches.open(CACHE).then((cache) => {
    return cache.addAll([
      '/',
      '/expenses/static/dist/css/base.css',
      '/expenses/static/dist/css/bootstrap.min.css',
      '/expenses/static/dist/imgs/open-iconic/svg/pencil.svg',
      '/expenses/static/dist/js/bootstrap.bundle.min.js',
      '/expenses/static/dist/js/jquery-3.3.1.slim.min.js',
      '/list',
      '/static/imgs/hawk.png',
      '/static/imgs/icons/favicon.ico',
    ]);
  }).catch((error) => {
    console.log('Failed to populate cache with app shell:', error)
  });
}

function fromNetwork(request, timeout) {
  return new Promise(function (fulfill, reject) {
    var timeoutId = setTimeout(reject, timeout);
    fetch(request).then(function (response) {
      clearTimeout(timeoutId);
      fulfill(response);
    }, reject);
  });
}

function fromCache(request) {
  return caches.open(CACHE).then(function (cache) {
    return cache.match(request).then(function (matching) {
      return matching || Promise.reject('no-match');
    });
  });
}
