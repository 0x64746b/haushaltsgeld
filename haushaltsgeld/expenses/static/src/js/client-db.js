import { openDB } from 'idb';

const DATABASE = 'haushaltsgeld';
export const EXPENSE_STORE = 'expenses';

export function getDb() {
  return openDB(
    DATABASE,
    1,
    {
      upgrade(db, oldVersion, newVersion, transaction) {
        console.log(`Upgrading client-side DB '${DATABASE}' from v${oldVersion} to v${newVersion}`);
        console.log(' Creating object store for expenses');
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
}