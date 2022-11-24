import React, {useState} from 'react';
import '../css/main2.css';
import default_image from '../images/default_image.png';
import { Link } from 'react-router-dom';

function Main4(){
    return(
        <div>
            <div className = "contents">
                선택한 누끼가 이것이 맞나요 ?
            </div>
            <div>
                <img className='preview_image' src = {default_image}/>
            </div>
            <Link to='/main3'>
                <div className="reselect">
                    다시선택
                </div>
            </Link>
            <Link to = "/main5">
                <div className = "selected">
                    맞음
                </div>
            </Link>
        </div>
    );
}
export default Main4;