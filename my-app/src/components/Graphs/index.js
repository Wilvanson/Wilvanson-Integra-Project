import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { getGraph } from '../../store/graph'


const GraphPage = () => {
    const [items, setitems] = useState([])
    // const dispatch = useDispatch(); 

    const getGraph = async () => {
        const response = await fetch(`http://127.0.0.1:5000/api/data/`);
        console.log(response)
        
        if (response.ok) {
          let list = await response.json();
          let arr = []
          for (let key in list){
              let obj = list[key]
              obj['for'] = key
            //   obj[key] = list[key]
              arr.push(obj)
          }
          return arr

        }else{
          throw new Error(`${response.status}`)
        }
      };

      useEffect(() =>{
        getGraph().then(list => setitems(list))
      },[])

    //   console.log(items)
    
    return (
      <div>
          <p>Hello</p>
          {items.map((item) =>
            <div>
                <p>FOR: {item['for']}</p>
                <p>AVG: {item['AVG']}</p>
                <p>MAX: {item['MAX']}</p>
                <p>MIN: {item['MIN']}</p>
                <p>ARR: {item['RECORDS']}</p>
            </div>
          )}
          
      </div>
    );
  };
  
  export default GraphPage;