import React, {useState, useEffect, useCallback} from 'react';
import '../css/main5.css'
import Loading from './loading.js';
import axios from 'axios';
import Main6 from './main6.js';

function Main5(){
    const [loading, setLoading] = useState(true);
    let data = JSON.stringify({
        isConfirmed: true,
    });

    const mainApi = useCallback(async () => {
        // setLoading(true); // api 호출 전에 true로 변경하여 로딩화면 띄우기
        await axios.post("http://192.168.123.107:9091/mask?id="+sessionStorage.getItem('id'), data, {headers:{"Content-Type" : "application/json"}})
        .then((response)=> {
        if(response.data === "success"){
            console.log(response.data);
            setLoading(false);
        }
        else{
            alert("비디오 업로드 실패")
        }
    })
    }, [loading]);

    useEffect(() => {
        mainApi();
    }, [mainApi]);

    return(
        <div>
            {/* {loading && <Loading />} */}
            {loading ? <Loading /> : <Main6 />}
        </div>
        // <Loading />
        //<Main6/>
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
export default Main5;