import shortid from 'shortid';
import { openDB, deleteDB, wrap, unwrap } from 'idb';

var DATABASE = 'haushaltsgeld';
var EXPENSE_STORE = 'expenses';

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

async function storeExpense(expense) {
  const db = await openDB(
    DATABASE,
    1,
    {
      upgrade(db, oldVersion, newVersion, transaction) {
        console.log(`Upgrading DB from v${oldVersion} to v${newVersion}`);
        console.log('Creating the expenses object store');
        db.createObjectStore(EXPENSE_STORE, {keyPath: 'expenseId'});
      },
      blocked() {
        console.log('There are older versions of the database open on the origin, so this version cannot open')
      },
      blocking() {
        console.log('This connection is blocking a future version of the database from opening')
      }
    }
  );
  await db.put(EXPENSE_STORE, expense);
}