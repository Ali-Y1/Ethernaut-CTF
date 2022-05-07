# King

The goal is to trigger the `receive()` function so that it will send you ether. At the time, it sends you ether it will trigger the `fallback()` function which will consume all the gas and revert the transaction, so you will not receive any ether and the contract will stop working.
