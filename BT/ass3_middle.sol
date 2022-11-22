//SPDX-License-Identifier: MIT
pragma solidity ^0.6;
contract banking
{
    mapping(address=>uint) public user_account;
    mapping(address=>bool) public user_exists;
    function create_account() public payable returns(string memory)
    {
        require(user_exists[msg.sender]==false,'Account already created');
        if(msg.value==0)
        {
            user_account[msg.sender]=0;
            user_exists[msg.sender]=true;
            return "Account created";
        }
        require(user_exists[msg.sender]==false,"Account already created");
        user_account[msg.sender]=msg.value;
        user_exists[msg.sender]=true;
        return "Account created";
    }
    function deposit() public payable returns(string memory)
    {
        require(user_exists[msg.sender]==true,"Account not created");
        require(msg.value>0,"Value for deposit is Zero");
        user_account[msg.sender]=user_account[msg.sender]+msg.value;
        return "Deposited Successfully";
    }
    function withdraw(uint amount) public payable returns(string memory)
    {
        require(user_account[msg.sender]>amount,"Insufficient Balance");
        require(user_exists[msg.sender]==true,"Account not created");
        require(amount>0,"Amount should be more than zero");
        user_account[msg.sender]=user_account[msg.sender]-amount;
        msg.sender.transfer(amount);
        return "Withdrawl Successful";
    }
    function user_balance() public view returns(uint)
    {
        return user_account[msg.sender];
    }
}