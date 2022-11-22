// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract Student_management{

    event log(string func);
    
    fallback() external payable{
        emit log('fallback');
    }

    struct Student{
        int stu_id;
        string Name;
        string department;
    }

    Student[] students;

    function add_stud(int stu_id,string memory Name, string memory department) public{
        Student memory stud = Student(stu_id,Name,department);
        students.push(stud);
    }

     function get_stud(int stu_id) public view returns(string memory,string memory){
        for(uint i=0;i<students.length;i++){
            Student memory stud = students[i];
            if(stud.stu_id== stu_id){
            return(stud.Name,stud.department);
        }
     }
 
     }
}