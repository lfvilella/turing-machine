import React from 'react';
import './cards_style.css';

const Card = props => {
    return(
        <div className="card text-center shadow">
            <div className="overflow">
                <img src={props.imgsrc} alt="Image turing machine I" className="card-img-top"/>
            </div>
            <div className="card-body text-dark">
                <h4 className="card-title">{props.title}</h4> 
                <p className="card-text text-secondary">
                    {props.description}
                </p> 
                <a href="#" className="btn btn-outline-success">Go turing machine</a> 
            </div>
        </div>
    );
}

export default Card;