import React, { useState } from 'react';

import './cards_style.css';

const axios = require('axios');
axios.defaults.baseURL = 'http://localhost:8000/api/v.1';
axios.defaults.headers.post['Content-Type'] = 'application/json';

const Card = props => {
  const [tapeData, setTapeData] = useState('');
  const [machineResult, setMachinerResult] = useState({});

  function sendTape() {
    return axios.post(
      `/machine/${props.pathUrl}`, { "tape": tapeData }
    ).then((response) => {
      setMachinerResult(response.data)
      // console.log(response);
    }).catch((error) => {
      console.log(error);
    })
  }

  const renderResult = () => {
    return (
      <div className='output'>
        <h6 className="OutputText">Output: <b>{machineResult.output}</b></h6>
        <ul className="TransitionsText">
          Transitions: 
          {(machineResult.transitions || []).map(transition => (
            <li>{JSON.stringify(transition)}</li>
          ))}
        </ul>
        <p className="TapeText">Tape: {machineResult.tape}</p>
        <p className="MessageText">Message: {machineResult.message}</p>
        {/* <p>{JSON.stringify(machineResult)}</p> */}
      </div>
    )
  }

  return (
    <div className="card text-center shadow">
      <div className="overflow">
        <img src={props.imgsrc} alt="Image turing machine I" className="card-img-top" />
      </div>
      <div className="card-body text-dark">
        <h4 className="card-title">{props.title}</h4>
        <p className="card-text text-secondary">
          {props.description}
        </p>
        <hr />
        <div>
          <h6>Insert the tape below to test the machine!</h6>
          {/* <input type="text" name="" id="" placeholder={props.placeholder} /> */}
          <input className="input" type="text" name="tapeData" value={tapeData} onChange={e => setTapeData(e.target.value)} placeholder={props.placeholder} />
          <br /><br />
          <button onClick={sendTape} className="btn btn-outline-success">Run Machine</button>
        </div>
        <hr/>
        {renderResult()}
      </div>
    </div>
  );
}

export default Card;
