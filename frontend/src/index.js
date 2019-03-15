import React from 'react';
import ReactDOM from 'react-dom';
import Root from './Root';
import { createStore, applyMiddleware } from 'redux';
import { Provider } from 'react-redux';
import * as serviceWorker from './serviceWorker';
import { createPromise } from 'redux-promise-middleware';
import modules from './store/modules';

const devTools = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__;

const customizedPromiseMiddleware = createPromise({
  promiseTypeSuffixes: ['LOADING', 'SUCCESS', 'FAILURE']
});

const store = createStore(modules, devTools(applyMiddleware(customizedPromiseMiddleware)))


ReactDOM.render(
  <Provider store={store}>
    <Root />
  </Provider>,
 document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
