import React from 'react';
import './cards_style.css';

const axios = require('axios');
axios.defaults.baseURL = 'http://localhost:8000/api/v.1';
axios.defaults.headers.post['Content-Type'] = 'application/json';

const Card = props => {
  let tapeData = '';
  let machineResult = '';

  function sendTape() {
    return axios.post(
      `/machine/${props.pathUrl}`, { "tape": tapeData }
    ).then((response) => {
      machineResult = response;
      console.log(response);
    }).catch((error) => {
      console.log(error);
    })
  }

  const renderResult = () => {
    if (machineResult !== '') {
      return (
        <div>
          <br />
          <h6>Saida:</h6>
          <p>{machineResult}</p>
        </div>
      )
    }
  }

  function handleTapeData(e) {
    tapeData = e.target.value
    console.log(tapeData);
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
          <h6>Insira na fita abaixo para testar a máquina!</h6>
          {/* <input type="text" name="" id="" placeholder={props.placeholder} /> */}
          <input type="text" name="tapeData" onChange={handleTapeData} placeholder={props.placeholder} />
          <br /><br />
          <button onClick={sendTape} className="btn btn-outline-success">Run Machine</button>
        </div>
        {renderResult()}
      </div>
    </div>
  );
}

export default Card;
