import React, {useState} from 'react';
import '../css/main2.css';
import default_image from '../images/default_image.png';
import { Link } from 'react-router-dom';
import GetXY from './getXY.js';
import GetImage from './getImage.js';

function Main3(){
    const [file, setFile] = useState({
        preview_image: {default_image},
    });
    // coordinateX: '', //사용자 마우스 클릭한 좌표 저장
    // coordinateY: '',

    // const imageOverlay = e => { 
    // setFile(prev => ({
    // ...prev,
    // preview_image: {default_image},
    // coordinateX:
    //   ((e.nativeEvent.offsetX ) / 900) * 100, // 가로가 900이라..
    // coordinateY:
    //   ((e.nativeEvent.offsetY ) / 570) *100, // 세로가 570이라..
    // }));
    // };
    // console.log(file.coordinateX);
    // console.log(file.coordinateY);

    return(
        <div>
            <div className = "contents">
                비디오에서 삭제하고 싶은 사물 / 사람의 누끼를 골라주세요 !
            </div>
            <Link to='/main4'>
                <div>
                    <img className='preview_image' src = {default_image} onClick= {e=>{GetXY(e)}}/>
                </div>
            </Link>
            {/* <Link to = "/main4">
                <div className = "selected">
                    완료
                </div>
            </Link> */}
        </div>
    );
}
export default Main3;