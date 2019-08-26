Vue.component(
    'expense-editor',
    {
        data: function () {
            return {
                amount: null,
                store: "unspecified",
                date: this.today(),
            }
        },
        methods: {
            today: function () {
                return new Date().toISOString().split('T')[0]
            }
        },
        template: `
          <form method="post">
            <div class="form-group" style="position: relative;">
              <label for="amount">Amount</label>
              <input v-model="amount" aria-describedby="amountHelp" id="amount" min="0.01" name="amount" placeholder="15.98" required="required" step="0.01" type="number" class="form-control">
              <ul class="invalid-tooltip" style="padding-left: 1.3rem;"></ul> 
              <small id="amountHelp" class="form-text text-muted">The amount of money you spent</small>
            </div>
            <div class="form-group" style="position: relative;">
              <label for="store">Store</label>
              <select v-model="store" aria-describedby="storeHelp" id="store" name="store" class="form-control">
                <option value="unspecified">Unspecified</option>
                <option value="aldi">Aldi</option>
                <option value="lidl">Lidl</option>
                <option value="rewe">Rewe</option>
                <option value="edeka">Edeka</option>
                <option value="budni">Budni</option>
                <option value="other">Other</option>
              </select>
              <ul class="invalid-tooltip" style="padding-left: 1.3rem;"></ul>
              <small id="storeHelp" class="form-text text-muted">The grocery you shopped at</small>
            </div>
            <div class="form-group" style="position: relative;">
              <label for="date">Date</label> 
              <input v-model.date="date" aria-describedby="dateHelp" id="date" v-bind:max="today()" name="date" required="required" type="date" class="form-control"> 
              <ul class="invalid-tooltip" style="padding-left: 1.3rem;"></ul> 
              <small id="dateHelp" class="form-text text-muted">The day you spent the money</small>
            </div>
            <input id="submit" name="submit" type="submit" value="Record" class="btn btn-primary">
          </form>`
    }
)