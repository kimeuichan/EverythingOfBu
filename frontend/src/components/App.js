import React, { Component, Fragment } from 'react';
import { Route, Switch } from 'react-router-dom';
import { Post } from '../pages';


class App extends Component {
  render() {
    return (
      <Fragment>
        <Switch>
          <Route exact path="/" component={Post}/>
        </Switch>
      </Fragment>
    );
  }
}

export default App;
