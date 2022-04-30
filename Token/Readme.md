# Token
This contract can be exploited by causing underflow in math calculation.
### Steps
1. Get the current balance 
2. Send the current balance + 1 to another user
3. Congrats you have infinity tokens
#### What happened:
This contract is of version 0.6.0 and is not using safe math which has a bug that cause underflow , overflow during calculation.
By sending current balance + 1 this will cause an underflow passing the `require` and an underflow in `balances[msg.sender] -= _value` giving `balances[msg.sender]` the maximum number in `uint`.  