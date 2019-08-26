var CACHE = 'network-or-cache';

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

function cacheAppShell() {
  return caches.open(CACHE).then((cache) => {
    return cache.addAll([
      '/',
      '/expenses/static/css/base.css',
      '/expenses/static/css/bootstrap.min.css',
      '/expenses/static/imgs/open-iconic/svg/pencil.svg',
      '/expenses/static/js/bootstrap.bundle.min.js',
      '/expenses/static/js/jquery-3.3.1.slim.min.js',
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
