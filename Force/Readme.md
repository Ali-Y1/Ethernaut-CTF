# Force
This ctf can be easily solved by the method `selfdestruct(address)`.
### Steps:
1. Deploy attack contract.
2. Fund this contract with some ether.
3. self distruct this contract and send all the funds to the ctf contract.
### How is this possible:
By Calling `selfdistruct()` and passing address as a parameter the contract will be deleted from the blockchain and the ether in it will be forced to the address passed. 