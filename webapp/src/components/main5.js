import React from 'react';
import '../css/main2.css'
import HandleOutput from './getVideo.js';

function Main5(){
    return(
        <div>
            <div className = "contents">
                변환된 비디오를 다운로드하세요
            </div>
            {/* <video className = "videoDisplay" controls={true} autoPlay={true} type = "video/mp4" /> */}
            <div className = "selected" onClick={HandleOutput}>
                다운로드
            </div>
        </div>
    );
}
export default Main5;

//url로 줬을 때 fileDownload할 수 있는 방법중 하나. 가능할지는 아직..
// import axios from 'axios'
// import fileDownload from 'js-file-download'
// ...

// handleDownload = (url, filename) => {
//   axios.get(url, {
//     responseType: 'blob',
//   })
//   .then((res) => {
//     fileDownload(res.data, filename)
//   })
// }
 
// ...

// <button onClick={() => {this.handleDownload('https://your-website.com/your-image.jpg', 'test-download.jpg')
// }}>Download Image</button>