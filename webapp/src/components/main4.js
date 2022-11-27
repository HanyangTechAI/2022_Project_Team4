import React, {useState, useEffect} from 'react';
import '../css/main2.css';
import default_image from '../images/default_image.png';
import { Link } from 'react-router-dom';
import axios from 'axios';
import Ok from './ok.js';

function Main4(){
    const [file, setFile] = useState({
        preview_image: {default_image},
    });

    useEffect(() => {
        axios.get("http://172.16.166.231:9091/mask?id="+sessionStorage.getItem('id'), {responseType: 'blob'}).then(
        (response)=> {
            console.log(response);
            console.log(response.data);
            const fileReader = new FileReader();
            fileReader.readAsDataURL(response.data)
            fileReader.onload = () => {
            const previewImage = fileReader.result;
            console.log(previewImage);
            setFile({
                preview_image: previewImage,
        })
    }})
    },[]);

    // let data = JSON.stringify({
    //     hihi: 3,
    // });

    //http://192.168.0.19:9091/region?id=
    // if(file.preview_image == default_image){
        // axios.get("http://172.16.166.231:9091/region?id="+sessionStorage.getItem('id')).then(
        // (response)=> {
        //     // const fileReader = new FileReader();
        //     // fileReader.readAsDataURL(response.data)
        //     // fileReader.onload = () => {
        //     // const previewImage = response.data;
        //     setFile({
        //         preview_image: response.data,
        //     })
        // })
    // }
    //url로 받으면 setFile하고 src에 그대로.

    return(
        <div>
            <div className = "contents">
                선택한 누끼가 이것이 맞나요 ?
            </div>
            <div>
                <img className='preview_image' src = {file.preview_image}/>
            </div>
            <Link to='/main3'>
                <div className="reselect">
                    다시선택
                </div>
            </Link>
            <Link to = "/main5">
                <div className = "selected" onClick={Ok}>
                    맞음
                </div>
            </Link>
        </div>
    );
}
export default Main4;