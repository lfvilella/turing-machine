import React, {Component} from 'react';
import Card from './cards';

import img_turing_machine_I from '../assets/turing-machine-I.png';
import img_turing_machine_II from '../assets/turing-machine-II.jpg';
import img_turing_machine_III from '../assets/turing-machine-III.jpg';

class multipleCards extends Component {
    render() {
        return(
            <div className="container justify-content-center">
                <div className="row">
                    <div className="col-md-4">
                        <Card 
                            imgsrc={img_turing_machine_I} 
                            title="Turing Machine I"
                            description="This is a very beautiful turing machine.

                            Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
                            Mollitia perferendis aut deleniti pariatur asperiores 
                            laboriosam voluptatum quidem modi enim minima dolores maxime, 
                            eum quo minus nisi aliquid tempore iusto eaque?"/>
                    </div>
                    <div className="col-md-4">
                        <Card 
                            imgsrc={img_turing_machine_II} 
                            title="Turing Machine II"
                            description="This is a very beautiful turing machine.

                            Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
                            Mollitia perferendis aut deleniti pariatur asperiores 
                            laboriosam voluptatum quidem modi enim minima dolores maxime, 
                            eum quo minus nisi aliquid tempore iusto eaque?"/>
                    </div>
                    <div className="col-md-4">
                        <Card 
                            imgsrc={img_turing_machine_III} 
                            title="Turing Machine III"
                            description="This is a very beautiful turing machine.

                            Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
                            Mollitia perferendis aut deleniti pariatur asperiores 
                            laboriosam voluptatum quidem modi enim minima dolores maxime, 
                            eum quo minus nisi aliquid tempore iusto eaque?"/>
                    </div>
                </div>
                
                <div className="row">
                    <div className="col-md-4">
                        <Card 
                            imgsrc={img_turing_machine_I} 
                            title="Turing Machine I"
                            description="This is a very beautiful turing machine.

                            Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
                            Mollitia perferendis aut deleniti pariatur asperiores 
                            laboriosam voluptatum quidem modi enim minima dolores maxime, 
                            eum quo minus nisi aliquid tempore iusto eaque?"/>
                    </div>
                    <div className="col-md-4">
                        <Card 
                            imgsrc={img_turing_machine_II} 
                            title="Turing Machine II"
                            description="This is a very beautiful turing machine.

                            Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
                            Mollitia perferendis aut deleniti pariatur asperiores 
                            laboriosam voluptatum quidem modi enim minima dolores maxime, 
                            eum quo minus nisi aliquid tempore iusto eaque?"/>
                    </div>
                    <div className="col-md-4">
                        <Card 
                            imgsrc={img_turing_machine_III} 
                            title="Turing Machine III"
                            description="This is a very beautiful turing machine.

                            Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
                            Mollitia perferendis aut deleniti pariatur asperiores 
                            laboriosam voluptatum quidem modi enim minima dolores maxime, 
                            eum quo minus nisi aliquid tempore iusto eaque?"/>
                    </div>
                </div>
            </div>
        );
    }
}

export default multipleCards;