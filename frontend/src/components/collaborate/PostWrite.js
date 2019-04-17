import React, { Component } from 'react'
import { List, Record } from 'immutable';

const Member = Record({
  type: 0,
});

const MemberList = ({handleChange, index, handleRemove}) => {
  return (
    <div>
      <select name={`members[${index}]`} onChange={(evt) => handleChange(evt, index)}>
        <option value="0">개발자</option>
        <option value="1">디자이너</option>
        <option value="2">PM</option>
      </select>
      <button type="button" onClick={(evt) => handleRemove(index)}>삭제</button>
    </div>
  );
}

export default class PostWrite extends Component {
  constructor(props){
    super();
    this.state = {
      members : List([
        Member({type: 0}),
      ]),  
    };
  }

  handleSubmit = (event) => {
    event.preventDefault();
    if(this.state.members.size < 1){
      alert("멤버를 추가해주세요");
      return;
    }

    const { createPost } = this.props;
    
    const data = new FormData(event.target);
    let jsonObject = {};

    for (const [key, value]  of data.entries()) {
        jsonObject[key] = value;
    }
    console.log(jsonObject);
  }

  addMember = () => {
    this.setState({
      members: this.state.members.push(Member())
    });
  }

  handleChange = (evt, index) => {
    this.setState({
      members: this.state.members.update(index, value => evt.target.value)
    });
  }

  handleRemove = (index) => {
    if(this.state.members.size < 2){
      alert("최소한 한명의 멤버는 존재해야 합니다");
      return;
    }

    this.setState({
      members: this.state.members.remove(index)
    });
  }

  render() {
    // const { commitEvt } = this.props;
    const memberList = this.state.members.map((item, i)=> { 
      return (<MemberList key={i} index={i} 
                          handleChange={this.handleChange} data={item} 
                          handleRemove={this.handleRemove} />); 
    });

    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <input name='title' placeholder="글 제목"/>
          <textarea name='description' placeholder="글 제목"/>
          {memberList}
          <button type="button" onClick={this.addMember}>멤버 추가</button>
          <button type="submit">글쓰기</button>
        </form>
      </div>
    )
  }
}
