import React from 'react';
import { NavLink } from 'react-router-dom';
import {useSelector} from 'react-redux';

const NavBar = () => {
  return (
    <nav>
      <ul className='navbar'>
        <li>
          <NavLink className='links' to='/' exact={true} activeClassName='active'>
            Attributes
          </NavLink>
        </li>
        <li>
          <NavLink className='links' to='/medvCrim' exact={true} activeClassName='active'>
            Crime
          </NavLink>
        </li>
        <li>
          <NavLink className='links' to='/medvAge' exact={true} activeClassName='active'>
            Age
          </NavLink>
        </li>
        <li>
          <NavLink className='links' to='/medvPtratio' exact={true} activeClassName='active'>
            Pupil-Teacher Ratio
          </NavLink>
        </li>
        <li>
        <a className='links' href="https://github.com/Wilvanson" target="_blank">
          GitHub
        </a>
      </li>
      <li>
        <a className='links' href="https://www.linkedin.com/in/wilvanson-dutervil-509a2b174/" target="_blank">
          Linkedin
        </a>
      </li>
        
      </ul>
    </nav>
  );
}

export default NavBar;