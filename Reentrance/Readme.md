# Re-entrancy

The Reentrancy attack is one of the most destructive attacks in the Solidity smart contract. A reentrancy attack occurs when a function makes an external call to another untrusted contract. Then the untrusted contract makes a recursive call back to the original function in an attempt to drain funds.

## Steps:

1. Attacker deploys a malicious contract.
2. Attacker stores some eth using `donate()` from the malicious contract.
3. Now the contract can withdraw some money.
4. The attacker will withdraw some money using the contract but a `fallback` or `recieve` function will call the `withdraw` function again and so on till the funds are drained.

All that happened before the contract subtract the drawn amount from the attacker balance.

The vulnerability comes where we send the user their requested amount of ether. In this case, the attacker calls withdraw() function. Since his balance has not yet been set to 0, he is able to transfer the tokens even though he has already received tokens.

## How to Protect Smart Contract Against a Reentrancy Attack?

To prevent a reentrancy attack in a Solidity smart contract, you should:

- Ensure all state changes happen before calling external contracts, i.e., update balances or code internally before calling external code

- Use function modifiers that prevent reentrancy
