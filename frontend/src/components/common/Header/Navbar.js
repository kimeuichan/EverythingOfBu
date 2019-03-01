import React, { Component } from 'react'
import { Link } from 'react-router-dom';

export default class Navbar extends Component {
  render() {
    return (
      <nav>
        <ul>
          <li><Link to="/">Main</Link></li>
        </ul>
		  </nav>
    )
  }
}
