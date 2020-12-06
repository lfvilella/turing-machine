import React, { Component } from 'react';
import Card from './cards';

import img_turing_machine_I from '../assets/turing-machine-I.png';
import img_turing_machine_II from '../assets/turing-machine-II.jpg';
import img_turing_machine_III from '../assets/turing-machine-III.jpg';

class multipleCards extends Component {
  render() {
    return (
      <div className="container justify-content-center">
        <div className="row">
          <div className="col-md-4">
            <Card
              imgsrc={img_turing_machine_I}
              title="Fibonacci Machine"
              description="Esta máquina valida sequências de fibonacci."
              pathUrl="fibonacci"
              placeholder="1|2|3|5|8|13|21" />
          </div>
          <div className="col-md-4">
            <Card
              imgsrc={img_turing_machine_II}
              title="Triple Balancing Machine"
              description="Esta máquina valida o problema básico de triplo balanceamento."
              pathUrl="triple_balancing"
              placeholder="a|a|b|b|c|c" />
          </div>
          <div className="col-md-4">
            <Card
              imgsrc={img_turing_machine_III}
              title="Odd Machine"
              description="Esta máquina transforma todo número par em '1'"
              pathUrl="odd"
              placeholder="1|2|3|4|5|10|20" />
          </div>
        </div>
      </div>
    );
  }
}

export default multipleCards;
