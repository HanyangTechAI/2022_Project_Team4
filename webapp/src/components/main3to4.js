import React, {useState, useEffect, useCallback} from 'react';
import '../css/main5.css'
import default_image from '../images/default_image.png';
import Loading from './loading.js';
import axios from 'axios';
import Main4 from './main4.js';

function Main3to4(){
    const [file, setLoading] = useState({
        loading : true,
        preview_image: {default_image}
    });
    // let data = JSON.stringify({
    //     isConfirmed: true,
    // });

    const mainApi = useCallback(async () => {
        // setLoading(true); // api 호출 전에 true로 변경하여 로딩화면 띄우기
        axios.get("http://192.168.123.108:9091/mask?id="+sessionStorage.getItem('id'), {responseType: 'blob'}).then(
        (response)=> {
            console.log(response);
            console.log(response.data);
            const fileReader = new FileReader();
            fileReader.readAsDataURL(response.data)
            fileReader.onload = () => {
            const previewImage = fileReader.result;
            console.log(previewImage);
            setLoading({
                preview_image: previewImage,
                loading: false,
        })
    }})
    }, [file]);

    useEffect(() => {
        mainApi();
    }, [mainApi]);

    return(
        <div>
            {/* {loading && <Loading />} */}
            {file.loading ? <Loading /> : <Main4 image = {file.preview_image}/>}
        </div>
        // <Loading />
        // <Main6/>
        // <div>
        //     <ul className = "main_changing">
        //             <li>
        //                 <div><h1>비디오 변환중…</h1></div>
        //                 <div>
        //                     <h2>
        //                         잠시만 기다려주세요
        //                     </h2>
        //                 </div>
        //                 {/* <!—Progression Bar—> */}
        //                 <div></div>
        //             </li>
        //         </ul>
        // </div>
    );
}
export default Main3to4;