import React, { Component } from 'react'

export default class PostWrite extends Component {
  addMember = () => {

  }

  render() {
    const { commitEvt } = this.props;
    return (
      <div>
        <input name='title' placeholder="글 제목"/>
        <textarea name='description' placeholder="글 제목"/>
        <button onClick={this.addMember}>멤버 추가</button>
        <button onClick={commitEvt}>저장</button>
      </div>
    )
  }
}
