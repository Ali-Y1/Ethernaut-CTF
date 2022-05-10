# GatekeeperTwo
This levels requires you to abuse a bad ERC20 implementation and control the NaughtCoin token.
## Steps:
1. call function approve with player address and  `INITIAL_SUPPLY` amount.
2. call function `transferFrom` with player address, any destination address ,and `INITIAL_SUPPLY` amount.
3. done
This contract has `lockTokens` modifier just on transfer, so we can use `approve` and `transferFrom` freely. 
