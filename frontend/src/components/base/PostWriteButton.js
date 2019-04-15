import React, { Component } from 'react'
import { Link } from 'react-router-dom';

export default class PostWriteButton extends Component {
  render() {
      const { toUrl } = this.props;
      return (
      <div>
        <Link to={toUrl}>글쓰기</Link>
      </div>
    )
  }
}
