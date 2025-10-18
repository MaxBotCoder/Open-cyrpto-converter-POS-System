//SPDX-License-Identifier: MIT
pragma solidity 0.8.0;

contract PosCode {

    //Variables
    address constant private adminAddress = 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4;
    address private userAddress;
    uint private totalBalance;

    //Mappings
    mapping(address => uint) private balanceAllocated;

    //Constructor
    constructor() {
        userAddress = msg.sender;
    }

    fallback() external payable {
        require(msg.value <= 10, "Gwei quantity cannot be lower than 10.");
        //Allocate whole balance.
        totalBalance = msg.value;
        //Allocating balance to admin.
        balanceAllocated[adminAddress] = totalBalance/10;
        //Send allocated quanitty to admin.
        payable(adminAddress).call{value: balanceAllocated[adminAddress]}("");
        //Allocate balance to user.
        balanceAllocated[userAddress] = totalBalance - balanceAllocated[adminAddress];
        //Send allocated quantity to user.
        payable(userAddress).call{value: balanceAllocated[userAddress]}("");
        //Update balance left
        totalBalance -= balanceAllocated[adminAddress];
        totalBalance -= balanceAllocated[userAddress];
    }

}
