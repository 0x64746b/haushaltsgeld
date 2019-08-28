import shortid from 'shortid';
import { EXPENSE_STORE, getDb } from './client-db';

if ('serviceWorker' in navigator) {
  navigator.serviceWorker.ready.then(function(registration) {
    console.log('Wiring click handler on expense editor button to sync events')
    $('#submit').on('click', event => {
        event.preventDefault();
        const expense = expenseFromForm($('#expenseEditor'));
        storeExpense(expense);
        return registration.sync.register(`expenseStored-${expense.expenseId}`)
        .then(
          console.log(`Requested sync for new expense ${expense.expenseId}`)
        ).catch(error => {
          console.log(`Failed to register sync request for new expense ${expense.expenseId}: ${error}`)
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

async function storeExpense(expense) {
  const db = await getDb();
  await db.put(EXPENSE_STORE, expense);
}