//SPDX-License-Identifier: MIT
pragma solidity ^0.6;
contract banking
{
    mapping(address=>uint) private user_account;
    function deposit(uint amount) public payable returns(string memory)
    {
        user_account[msg.sender] += amount;
        return "Deposited Successfully";
    }
    function withdraw(uint amount) public payable returns(string memory)
    {
        require(user_account[msg.sender]>amount,"Insufficient Balance");
        require(amount>0,"Amount should be more than zero");
        user_account[msg.sender]=user_account[msg.sender]-amount;
        return "Withdrawl Successful";
    }
    function user_balance() public view returns(uint)
    {
        return user_account[msg.sender];
    }
}