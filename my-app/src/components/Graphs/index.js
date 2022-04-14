import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import CanvasJSReact from '../../canvasjs-3.6.1/canvasjs.react';
var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;

const GraphPage = () => {
    const [items, setitems] = useState([])
    const [dataPoint, setDataPoints] = useState([])

    const getGraph = async () => {
        const response = await fetch(`/api/data/`);
        
        if (response.ok) {
          let list = await response.json();
          let arr = []
          for (let key in list){
              let obj = list[key]
              obj['for'] = key
              if(key !== 'ZYMEDVAGE' && key !== 'ZYMEDVPTRATIO' && key !== 'ZYMEDVCRIM'){
                let arr2 = list[key]['RECORDS'].sort((a, b) =>{
                  return a - b;
                })
                let point = arr2[Math.floor(arr2.length / 4)]
                let arr3 = arr2.slice(Math.floor(arr2.length / 2))
                let point2 = arr3[Math.floor(arr3.length / 2)]
                
                obj['Q1'] = point
                obj['Q2'] = point2
                
              }
              arr.push(obj)
          }
          return arr

        }else{
          throw new Error(`${response.status}`)
        }
      };

      useEffect(() =>{
        getGraph().then(list => {
          setitems(list)
          let arr =  [
                { label: list[0]['for'],  y: [list[0]['MIN'], list[0]['Q1'], list[0]['Q2'], list[0]['MAX'], list[0]['AVG']] },
                { label: list[1]['for'],  y: [list[1]['MIN'], list[1]['Q1'], list[1]['Q2'], list[1]['MAX'], list[1]['AVG']]  },
                { label: list[2]['for'],  y: [list[2]['MIN'], list[2]['Q1'], list[2]['Q2'], list[2]['MAX'], list[2]['AVG']]  },
                { label: list[3]['for'],  y: [list[3]['MIN'], list[3]['Q1'], list[3]['Q2'], list[3]['MAX'], list[3]['AVG']] },
                { label: list[4]['for'],  y: [list[4]['MIN'], list[4]['Q1'], list[4]['Q2'], list[4]['MAX'], list[4]['AVG']]  },
                { label: list[5]['for'],  y: [list[5]['MIN'], list[5]['Q1'], list[5]['Q2'], list[5]['MAX'], list[5]['AVG']]  },
                { label: list[6]['for'],  y: [list[6]['MIN'], list[6]['Q1'], list[6]['Q2'], list[6]['MAX'], list[6]['AVG']] },
                { label: list[7]['for'],  y: [list[7]['MIN'], list[7]['Q1'], list[7]['Q2'], list[7]['MAX'], list[7]['AVG']]  },
                { label: list[8]['for'],  y: [list[8]['MIN'], list[8]['Q1'], list[8]['Q2'], list[8]['MAX'], list[8]['AVG']]  },
                { label: list[9]['for'],  y: [list[9]['MIN'], list[9]['Q1'], list[9]['Q2'], list[9]['MAX'], list[9]['AVG']] },
                { label: list[10]['for'],  y: [list[10]['MIN'], list[10]['Q1'], list[10]['Q2'], list[10]['MAX'], list[10]['AVG']]  },
                { label: list[11]['for'],  y: [list[11]['MIN'], list[11]['Q1'], list[11]['Q2'], list[11]['MAX'], list[11]['AVG']]  },
                { label: list[12]['for'],  y: [list[12]['MIN'], list[12]['Q1'], list[12]['Q2'], list[12]['MAX'], list[12]['AVG']] }
                ]
          setDataPoints(arr)})
      
      },[])

      const options = {
        theme: "light2",
        animationEnabled: true,
        title:{
            text: "Integra HousingData"
        },
        data: [{
            type: "boxAndWhisker",
            yValueFormatString: "#,##0.## \"\"",
            dataPoints: dataPoint
        }]
    }
    
    
    return (
      <div className='charts'>
          <CanvasJSChart options={options} />
      </div>
    );
  };
  
  export default GraphPage;