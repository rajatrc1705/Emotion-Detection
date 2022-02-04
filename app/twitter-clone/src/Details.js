import axios from 'axios';
import React from 'react'
import {useState,useEffect} from 'react'

const Details=()=>{
const [data,setData]=useState([]);
    useEffect(()=>{
 getData();
},[]);

const getData=async()=>{
    await axios.get('http://localhost:8000/wel/')
    .then(res => {
        setData(res.data); 
        });
    }
   
    return data;

};
    
export default Details
       
        
   
