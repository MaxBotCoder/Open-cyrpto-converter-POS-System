//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PosSide {

    //Variables
    address public lastToInteract;
    address constant private adminAddress = EnterAdminAddressHere;
    address public userAddress;
    uint public totalBalance;

    //debugging variables
    uint public amountSentToUser;
    uint public amountSentToAdmin;

    //mapping
    mapping(address => uint) public moneyReservedForWhom;

    //constructor
    constructor() {
        userAddress = msg.sender;
    }
    
    fallback() external payable {
        lastToInteract = msg.sender; 
        totalBalance += msg.value;
        moneyReservedForWhom[userAddress] = msg.value/10;
        payable(userAddress).call{value: moneyReservedForWhom[userAddress]}("");
        amountSentToAdmin = totalBalance -= moneyReservedForWhom[userAddress];
        totalBalance -= moneyReservedForWhom[userAddress];
        payable(adminAddress).call{value: totalBalance}("");
        amountSentToUser = totalBalance;
        totalBalance -= totalBalance;
    }

}
