import React, { Component } from 'react'
import { Header } from './Header';



export default class AppTemplate extends Component {
  render() {
    const { children } = this.props;
    return (
      <div>
        <Header />
        { children }
      </div>
    )
  }
}

