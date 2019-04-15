import React, { Component } from 'react';
import { Route, Switch } from 'react-router-dom';
import { PostList, PostDetail, PostWrite } from '../pages';
import AppTemplate from './common/AppTemplate';


class App extends Component {
  render() {
    return (
      <AppTemplate>
        <Switch>
          <Route exact path="/collaborate/posts/:pageId?" component={PostList}/>
          <Route exact path="/collaborate/post" component={PostWrite}/>
          <Route exact path="/collaborate/post/:postId?" component={PostDetail}/>
        </Switch>
      </AppTemplate>
    );
  }
}

export default App;
