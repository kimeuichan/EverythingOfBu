import React, { Component } from 'react'
import axios from 'axios';

export default class PostView extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: '',
    }
  }

  componentDidMount = () => {
    const { match } = this.props;
    const self = this;
    axios.get(`http://localhost/api/collaborate/post/14`).then(function(res){
      // axios.get(`http://localhost/api/collaborate/post/${match.params.postId}`).then(function(res){
      console.log(res);
      self.setState({data: res.data})
    })
  }

  render() {
    console.log(this.state);
    if(!this.state.data)
      return <h1>로딩 중</h1>
    const {title, description, writter, created_time, isAlive, members} = this.state.data;
    return (
      <div className="ListItem">
        {title}
        {description}
      </div>
    )
  }
}


// export function PostView({item}) {
//   return (
//     <div className="ListItem">
//       <div className="item">{item.id}</div>
//       <div className="item">{item.title}</div>
//       <div className="item">{item.created_time}</div>
//     </div>
//   )
// }