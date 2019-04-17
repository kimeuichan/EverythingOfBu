import { handleActions } from 'redux-actions';
import { API_SERVER } from '../../settings';
import client from '../../lib/ApiClient';

function getPostListAPI(page){
  return client.get(`${API_SERVER}/api/collaborate/post?page=${page}`);
}

function getPostAPI(postId){
  return client.get(`${API_SERVER}/api/collaborate/post/${postId}`);
}

function createPostAPI(data){
  return client.post(`${API_SERVER}/api/collaborate/post`, data);
}

const GET_POST_LIST = 'GET_POST_LIST';
const GET_POST_LIST_PENDING = 'GET_POST_LIST_PENDING';
const GET_POST_LIST_SUCCESS = 'GET_POST_LIST_SUCCESS';
const GET_POST_LIST_FAILURE = 'GET_POST_LIST_FAILURE';

const GET_POST = 'GET_POST';
const GET_POST_PENDING = 'GET_POST_PENDING';
const GET_POST_SUCCESS = 'GET_POST_SUCCESS';
const GET_POST_FAILURE = 'GET_POST_FAILURE';

const CREATE_POST = 'CREATE_POST';
const CREATE_POST_PENDING = 'CREATE_POST_PENDING';
const CREATE_POST_SUCCESS = 'CREATE_POST_SUCCESS';
const CREATE_POST_FAILURE = 'CREATE_POST_FAILURE';


export const getPostList = (page) => ({
  type: GET_POST_LIST,
  payload: getPostListAPI(page)
});

export const createPost = (data) => ({
  type: CREATE_POST,
  payload: createPostAPI(data),
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
    return {
      ...state,
      pending: false,
      error: true,
      postList: []
    };
  }
}, initialState);
