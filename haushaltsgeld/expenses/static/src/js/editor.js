import { Expense, storeExpense } from './client-db';

if ('serviceWorker' in navigator) {
  console.log('Waiting for service worker to become ready...')
  navigator.serviceWorker.ready.then(registration => {
    console.log(' Wiring click handler on expense editor button to sync events')
    $('#submit').on('click', event => {
      event.preventDefault();
      const expense = Expense.fromForm($('#expenseEditor'));
      storeExpense(expense).then(_ => {
        console.log(`Requesting sync of expense ${expense}`);
        registration.sync.register(`expenseStored-${expense.id}`).then(
          console.log(` Requested sync for expense ${expense.id}`)
        ).catch(error => {
          console.log(` Failed to register sync request for expense ${expense.id}: ${error}`)
        })
      });
    })
  }).catch(error => {
    console.log(`Service worker did not become ready: ${error}`);
  });
}