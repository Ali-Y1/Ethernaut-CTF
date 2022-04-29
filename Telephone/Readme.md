# Telephone
This game is easy to win all you have to do is call `changeOwner` from a contract and pass your address.
#### What happened:
The only condition that forbiden you from taking ownership is `tx.origin != msg.sender`.
So by using a contract `tx.origin` will be the user address while `msg.sender` will be that of the contract. 
