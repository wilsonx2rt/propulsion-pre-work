function Bank() {
  this.customers = {};
}

Bank.prototype.addCustomer = function(customerName) {
  this.customers[customerName] = {account: 0};
  console.log(`A new account was successfully created for ${customerName}`);
}

Bank.prototype.printAccount = function(customerName) {
  console.log(`${customerName}\'s current account balance is ${this.customers[customerName].account}`);
}

Bank.prototype.deposit = function(customerName, depositAmount) {
  this.customers[customerName].account += depositAmount;
  console.log(`${customerName}'s transaction was successfully executed`);
  this.printAccount(customerName);
}

Bank.prototype.withdraw = function(customerName, withdrawAmount) {
  if(this.customers[customerName].account - withdrawAmount >= 0) {
    this.customers[customerName].account -= withdrawAmount;
    console.log(`${customerName}'s transaction was successfully executed`);
    this.printAccount(customerName);
  } else {
    console.log('There aren\'t enough funds to complete the transaction');
    this.printAccount(customerName);
  }
}

Bank.prototype.closeAccount = function(customerName) {
  var accountBalance = this.customers[customerName].account;
  if(accountBalance > 0) {
    this.withdraw(customerName, accountBalance);
    delete this.customers[customerName];
  } else {
    delete this.customers[customerName];
  }
  console.log(`${customerName}'s account has been closed`);
}

Bank.prototype.printAll = function() {
  var names =Object.keys(this.customers);
  names.forEach(name =>{
    console.log(`${name}'s current account balance is ${this.customers[name].account}`);
  })
}

var bank = new Bank();
bank.addCustomer('Sheldor');
// bank.printAccount('Sheldor');
bank.deposit('Sheldor', 10);
// bank.printAccount('Sheldor');
bank.addCustomer('Raj');
bank.printAccount('Raj');
bank.deposit('Raj', 10000);
//bank.printAccount('Raj');
bank.withdraw('Raj', 100);
bank.printAccount('Sheldor'); // this should print 'Sheldor account is 10'
bank.printAccount('Raj'); // this should print 'Raj account is 9900'
bank.withdraw('Sheldor', 10);
bank.printAll();
bank.closeAccount('Sheldor');
