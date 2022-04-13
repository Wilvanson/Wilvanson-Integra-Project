const LOAD_GRAPH = 'graph/loadGraph';

const loadGraph = items => {
    return {
      type: LOAD_GRAPH,
      items
    }
}

export const getGraph = () => async dispatch => {
    const response = await fetch(`/api/data`);
    
    if (response.ok) {
      const list = await response.json();
      console.log(list)
      // dispatch(loadGraph(list));
    }
  };


  const initialState = {
    items: {}
  };

export default function graphReducer(state = initialState, action) {
    let newState
    switch (action.type) {
        case LOAD_GRAPH:
            newState = action.items
            
            return newState
        default:
      return state;
  }
}