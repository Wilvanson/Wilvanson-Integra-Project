import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import CanvasJSReact from '../../canvasjs-3.6.1/canvasjs.react';
//var CanvasJSReact = require('./canvasjs.react');
var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;

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

      const options = {
        theme: "light2",
        animationEnabled: true,
        title:{
            text: "Integra HousingData"
        },
        axisY: {
            title: "Points"
        },
        data: [{
            type: "boxAndWhisker",
            yValueFormatString: "#,##0.# \"kcal/100g\"",
            dataPoints: [
                { label: items['for'],  y: items['RECORDS'] },
                // { label: "Cake",  y: [252, 346, 409, 437, 374.5] },
                // { label: "Biscuit",  y: [236, 281.5, 336.5, 428, 313] },
                // { label: "Doughnut",  y: [340, 382, 430, 452, 417] },
                // { label: "Pancakes",  y: [194, 224.5, 342, 384, 251] },
                // { label: "Bagels",  y: [241, 255, 276.5, 294, 274.5] }
            ]
        }]
    }
    
    
    return (
      <div>
          <p>Hello</p>
          {/* {items.map((item) =>
            <div>
                <p>FOR: {item['for']}</p>
                <p>AVG: {item['AVG']}</p>
                <p>MAX: {item['MAX']}</p>
                <p>MIN: {item['MIN']}</p>
                <p>ARR: {item['RECORDS']}</p>
            </div>
          )} */}
          <CanvasJSChart options={options} />
      </div>
    );
  };
  
  export default GraphPage;