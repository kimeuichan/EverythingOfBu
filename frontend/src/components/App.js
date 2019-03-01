import React, { Component } from 'react';
import { Route, Switch } from 'react-router-dom';
import { Post } from '../pages';
import AppTemplate from './common/AppTemplate';


class App extends Component {
  render() {
    return (
      <AppTemplate>
        <Switch>
          <Route exact path="/" component={Post}/>
        </Switch>
      </AppTemplate>
    );
  }
}

export default App;
