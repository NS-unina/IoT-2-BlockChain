// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.8.0 <0.9.0;


contract aakash4dev{
    struct device { 
        string channelName;
        uint8 value;
    }

    event valueRequest(device iotData);
    function putdata(device memory d) public {
        emit valueRequest(d);     
    }
}

