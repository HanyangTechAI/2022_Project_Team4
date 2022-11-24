import React, { Component } from 'react';
import logo from '../images/logo.jpg'
import '../css/header.css'
import { Link } from 'react-router-dom';

class Header extends Component{
    render(){
        return(
            <div className='header'>
                <Link to ='/'>
                    <div className='logo'>
                        <img src = {logo}/>
                    </div>
                </Link>
                <Link to='/'>
                    <div className = 'name'>Hanyang univ AI study group</div>
                </Link>
                <ul className = 'nav'>
                    <li><a href = "#link_contact">CONTACT</a></li>
                </ul>
            </div>
        );
    }
}
export default Header;