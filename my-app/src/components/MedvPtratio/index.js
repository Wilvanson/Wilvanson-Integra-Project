import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import CanvasJSReact from '../../canvasjs-3.6.1/canvasjs.react';
var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;

const MedvPtratioPage = () => {
    const [items, setitems] = useState([])
    const [dataPoint, setDataPoints] = useState([])

    const getGraph = async () => {
        const response = await fetch(`http://127.0.0.1:5000/api/data/medvPtratio`);

        
        if (response.ok) {
          let list = await response.json();
          return list['data']

        }else{
          throw new Error(`${response.status}`)
        }
      };

      useEffect(() =>{
        getGraph().then(list => {
          setitems(list)
          setDataPoints(list.sort((a, b) =>{
            return a.x - b.x;
          }))
        })
      },[])

      const options = {
        animationEnabled: true,
        exportEnabled: true,
        theme: "light2", // "light1", "dark1", "dark2"
        title:{
            text: "Integra HousingData"
        },
        axisY: {
            title: "median value of the house"
        },
        axisX: {
            title: "pupil teacher ratio",
            interval: 1
        },
        data: [{
            type: "line",
            toolTipContent: "X:{x} Y:{y}",
            dataPoints: dataPoint
           
        }]
    }
    
    
    return (
      <div className='charts'>
          <CanvasJSChart options={options} />
      </div>
    );
  };
  
  export default MedvPtratioPage;