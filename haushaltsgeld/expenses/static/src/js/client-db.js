import shortid from 'shortid';
import { openDB } from 'idb';

const DATABASE = 'haushaltsgeld';
const EXPENSE_STORE = 'expenses';

export class Expense {
  constructor(amount, store, date) {
    this.id = shortid.generate();
    this.amount = amount;
    this.store = store;
    this.date = date;
  }

  static fromForm(form) {
    const obj = [].reduce.call(
      form.serializeArray(),
      (result, input) => {
        result[input.name] = input.value;
        return result;
      },
      {}
    );
    obj.id = shortid.generate();
    return Expense.fromObject(obj);
  }

  static fromObject(obj) {
    const instance = new Expense(parseFloat(obj.amount), obj.store, new Date(obj.date));
    instance.id = obj.id;
    return instance;
  }

  toString() {
    return `<Expense: ${this.amount}>`;
  }
}

function getDb() {
  return openDB(
    DATABASE,
    1,
    {
      upgrade(db, oldVersion, newVersion, transaction) {
        console.log(`Upgrading client-side DB '${DATABASE}' from v${oldVersion} to v${newVersion}`);
        console.log(' Creating object store for expenses');
        db.createObjectStore(EXPENSE_STORE, {keyPath: 'id'});
      },
      blocked() {
        console.log('There are older versions of the database open on the origin, so this version cannot open')
      },
      blocking() {
        console.log('This connection is blocking a future version of the database from opening')
      }
    }
  );
}

export async function storeExpense(expense) {
  const db = await getDb();
  db.put(EXPENSE_STORE, expense);
}

export async function fetchExpense(id) {
  const db = await getDb();
  const obj = await db.get(EXPENSE_STORE, id);
  return Expense.fromObject(obj);
}