import React from 'react'
import { Link } from 'react-router-dom';

const Navbar = (props) => {
  return (
    <nav>
      <ul>
        <li><Link to="/">Main</Link></li>
        <li><Link to="/collaborate">Collaborate</Link></li>
        <li><Link to="/test">Test</Link></li>
      </ul>
    </nav>
  )
}

export default Navbar;