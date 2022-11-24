import React, {useState} from 'react';
import '../css/main2.css'

function Main6(){
    return(
        <div>
            <div className = "contents">
                변환된 비디오를 다운로드하세요
            </div>
            <video className = "videoDisplay" controls={true} autoPlay={true} type = "video/mp4" />
            <div className = "selected">
                다운로드
            </div>
        </div>
    );
}
export default Main6;