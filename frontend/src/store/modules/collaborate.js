import { handleActions } from 'redux-actions';
import axios from 'axios';

function getPostListAPI(page){
  return axios.get(`http://localhost/api/collaborate/post?page=${page}`);
}

function getPostAPI(postId){
  return axios.get(`http://localhost/api/collaborate/post/${postId}`);
}

const GET_POST_LIST = 'GET_POST_LIST';
const GET_POST_LIST_PENDING = 'GET_POST_LIST_PENDING';
const GET_POST_LIST_SUCCESS = 'GET_POST_LIST_SUCCESS';
const GET_POST_LIST_FAILURE = 'GET_POST_LIST_FAILURE';



export const getPostList = (page) => ({
  type: GET_POST_LIST,
  payload: getPostListAPI(page)
});

const initialState = {
  pending: false,
  error: false,
  postList: [], 
};


export default handleActions({
  [GET_POST_LIST_PENDING]: (state, action) => {
    return {
      ...state,
      pending: true,
      error: false,
    }
  },

  [GET_POST_LIST_SUCCESS]: (state, action) => {
    console.log(action);
    return {
      ...state,
      pending: false,
      error: false,
      postList: action.payload.data.results,
    };
  },

  [GET_POST_LIST_FAILURE]: (state, action) => {
    console.log("here");
    return {
      ...state,
      pending: false,
      error: true,
      postList: []
    };
  }
}, initialState);
