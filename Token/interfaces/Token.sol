// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

interface Token {
  function transfer(address,uint) external returns (bool);
  function balanceOf(address) external view returns (uint);
}