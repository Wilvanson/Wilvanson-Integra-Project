import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import CanvasJSReact from '../../canvasjs-3.6.1/canvasjs.react';
//var CanvasJSReact = require('./canvasjs.react');
var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;

const MedvAgePage = () => {
    const [items, setitems] = useState([])
    // const dispatch = useDispatch(); 

    const getGraph = async () => {
        const response = await fetch(`http://127.0.0.1:5000/api/data/medvAge`);
        console.log(response)
        
        if (response.ok) {
          let list = await response.json();
        //   let arr = []
        //   for (let key in list){
        //       let obj = list[key]
        //       obj['for'] = key
        //     //   obj[key] = list[key]
        //       arr.push(obj)
        //   }
          return list

        }else{
          throw new Error(`${response.status}`)
        }
      };

      useEffect(() =>{
        getGraph().then(list => setitems(list))
      },[])

      const options = {
        animationEnabled: true,
        exportEnabled: true,
        theme: "light2", // "light1", "dark1", "dark2"
        title:{
            text: "Integra HousingData"
        },
        axisY: {
            title: "median value of the house",
            suffix: "%"
        },
        axisX: {
            title: "Age",
            prefix: "W",
            interval: 2
        },
        data: [{
            type: "line",
            toolTipContent: "Week {x}: {y}%",
            dataPoints: [
                { x: 1, y: 64 },
                { x: 2, y: 61 },
                { x: 3, y: 64 },
                { x: 4, y: 62 },
                { x: 5, y: 64 },
                { x: 6, y: 60 },
                { x: 7, y: 58 },
                { x: 8, y: 59 },
                { x: 9, y: 53 },
                { x: 10, y: 54 },
                { x: 11, y: 61 },
                { x: 12, y: 60 },
                { x: 13, y: 55 },
                { x: 14, y: 60 },
                { x: 15, y: 56 },
                { x: 16, y: 60 },
                { x: 17, y: 59.5 },
                { x: 18, y: 63 },
                { x: 19, y: 58 },
                { x: 20, y: 54 },
                { x: 21, y: 59 },
                { x: 22, y: 64 },
                { x: 23, y: 59 }
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
  
  export default MedvAgePage;