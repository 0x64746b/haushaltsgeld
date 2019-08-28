import shortid from 'shortid';
import { openDB, deleteDB, wrap, unwrap } from 'idb';

if ('serviceWorker' in navigator) {
  navigator.serviceWorker.ready.then(function(registration) {
    $('#submit').on('click', event => {
        event.preventDefault();
        let expense = expenseFromForm($('#expenseEditor'));
        storeExpense(expense);
        return registration.sync.register(`expenseStored-${expense.expenseId}`)
        .then(
          console.log('Registered sync event for new expense')
        ).catch(error => {
          console.log(`Failed to register sync event for new expense: ${error}`)
        })
    })
  });
}

function expenseFromForm(form) {
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
  var dbPromise = openDB(
    'haushaltsgeld',
    1,
    function(upgradeDb) {
      switch (upgradeDb.oldVersion) {
        case 0:
          // a placeholder case so that the switch block will
          // execute when the database is first created
          // (oldVersion is 0)
        case 1:
          console.log('Creating the expenses object store');
          upgradeDb.createObjectStore('expenses', {keyPath: 'expenseId'});
      }
    }
  );
}