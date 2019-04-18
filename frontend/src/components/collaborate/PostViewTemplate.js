import React, { Component } from 'react'
import PostView from './PostView';
import ApiClient from '../../lib/ApiClient';
import { API_SERVER } from '../../settings';
import { withRouter } from 'react-router-dom';

class PostViewTemplate extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: {},
    }
  }

  componentDidMount = () => {
    const { match } = this.props;
    ApiClient.get(`${API_SERVER}/api/collaborate/post/${match.params.postId}`).then( response => {
      this.setState({ data: {...response.data} } );
    });
  }

  render() {
    if(!this.state.data)
      return <h1>로딩 중</h1>
    return (
      <PostView data={{...this.state.data}}/>
    )
  }
}


export default withRouter(PostViewTemplate);