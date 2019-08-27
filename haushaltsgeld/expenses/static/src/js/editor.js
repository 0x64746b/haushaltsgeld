import shortid from 'shortid';

if ('serviceWorker' in navigator) {
  navigator.serviceWorker.ready.then(function(registration) {
    $('#submit').on('click', event => {
        event.preventDefault();
        let expense = formToObject($('#expenseEditor'));
        console.log('expense:', expense);
        return registration.sync.register('expenseRecorded')
        .then(
          console.log('Sent sync event for new expense')
        ).catch(error => {
          console.log(`Failed to send sync event for new expense: ${error}`)
        })
    })
  });
}

function formToObject(form) {
  let data = [].reduce.call(
    form.serializeArray(), 
    (result, input) => { 
      result[input.name] = input.value; 
      return result;
    }, 
    {}
  );
  data['expenseId'] = shortid.generate();
  return data;
}

function storeExpense(expense) {
  var db;
  var request = window.indexedDB.open('Haushaltsgeld', 1);
  request.onupgradeneeded = function(event) {
    db = event.target.result;

  };
  request.onsuccess = function(event) {
    db = event.target.result;
  };
  request.onerror = function(event) {
    console.log(`Failed to open IndexedDB to store expense: ${event.target.errorCode}`);
  };
}