import shortid from 'shortid';
import { storeExpense } from './client-db';

if ('serviceWorker' in navigator) {
  console.log('Waiting for service worker to become ready...')
  navigator.serviceWorker.ready.then(registration => {
    console.log(' Wiring click handler on expense editor button to sync events')
    $('#submit').on('click', event => {
      event.preventDefault();
      const expense = expenseFromForm($('#expenseEditor'));
      storeExpense(expense).then(_ => {
        console.log(`Requesting sync of expense ${expense.expenseId}`);
        registration.sync.register(`expenseStored-${expense.expenseId}`).then(
          console.log(` Requested sync for expense ${expense.expenseId}`)
        ).catch(error => {
          console.log(` Failed to register sync request for expense ${expense.expenseId}: ${error}`)
        })
      });
    })
  }).catch(error => {
    console.log(`Service worker did not become ready: ${error}`);
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