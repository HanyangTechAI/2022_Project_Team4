import React from 'react';
import './App.css'
import Header from './components/header.js';
import Footer from './components/footer.js'
import Main1 from './components/main1.js';
import Main2 from './components/main2.js';
import Main2to3 from "./components/main2to3.js"
import Main3 from './components/main3.js';
import Main3to4 from './components/main3to4.js';
import Main4 from './components/main4.js';
import Main4to5 from './components/main4to5.js';
import Main5 from './components/main5.js';
import {Route, Routes, Link } from "react-router-dom";

const App = () => {
  return (
    <>
      <Header/>
      <div className='main'>
          <Routes>
            <Route path="/" element={<Main1 />} />
            <Route path="/main2" element={<Main2 />} />
            <Route path="/main2to3" element = {<Main2to3/>} />
            <Route path="/main3" element={<Main3 />}/>
            <Route path="/main3to4" element = {<Main3to4/>} />
            <Route path="/main4" element={<Main4 />}/>
            <Route path="/main4to5" element={<Main4to5 />}/>
            <Route path="/main5" element={<Main5 />}/>
          </Routes>
      </div>
      <Footer/>
    </>
  );
};

export default App;


// import React, {Component, useState} from 'react';
// import './App.css';
// import axios from 'axios';

// class App extends Component{
//   constructor(props){
//     super(props);
    
//     this.state = {selectedFile: null, }
//     /*this.state = {
//       selectedFile : null,
//     }*/
//   }
//   handleFileInput(e){
//     this.setState({selectedFile : e.target.files[0],}); //file 하나만 받으니까 index 0으로
//   }
//   handlePost = async () => {
//     const formData = new FormData(); //Form Data 만들어서 
//     formData.append('file', this.state.selectedFile);  //file 담기
//     //formData에 담아서 서버에 보내기
//     const config = {
//       header: { 'content-type': 'multipart/form-data' },
//     }
//     await axios.post("http://127.0.0.1:5000/fileupload", formData, config).then( //(업로드할 경로, 보낼 것)
//     //127.0.0.1 local 컴퓨터 주소 5000 플라스크 기본 포트
//       (response) => {
//         if(response.data=="success"){
//           console.log(response.data)
//         }
//         else{
//           alert("비디오 업로드 실패")
//         }
//       }
//     )
//   }
//   handleOutput = async () => {
//     console.log(1);
//     return await axios.get({
//       //url: "http://~~" 파일 다운로드 요청 API
//       url: "http://127.0.0.1:5000/fileDownload/logo.jpg",
//       method: "GET",
//       responseType: "blob", //받아올 데이터 타입 정하기. blob = binary Large Object 큰 데이터들 다룰 때 사용. 이미지, 오디오, 영상 등
//     }
//     ).then((response) => {
//       const blob = new Blob([response.data]); //전달 받은 데이터를 blob으로 변환
//       const fileObjectUrl = window.URL.createObjectURL(blob);

//       const link = document.createElement("a");
//       link.href = fileObjectUrl;
//       link.style.display = "none";

//       link.download = "download_Success";
//       document.body.appendChild(link);
//       link.click();
//       link.remove();

//       window.URL.revokeObjectURL(fileObjectUrl);
//     });
//   }
//   test () {
//     console.log("test")
//   }
//   render(){
//     return(
//       <div>
//        <input type = "file" name = "file" onChange = {e => this.handleFileInput(e)}/>
//        <button onClick = {this.handlePost}>Submit</button>
//        <button onClick = {this.handleOutput}>Download</button>
//       </div>
//     )
//   }
// }
// export default App;

/*function App() {
  return (
    <div className="App">
      <button>
        
      </button>
    </div>
  );
}*/

 /*const [myName, setName] = useState("Yeonjin")
  
  function changeName(){
    setName(myName === "Yeonjin"? "NotYeonjin" : "Yeonjin");
  }

  return(
    <div>
      <h1>
        안녕하세요. {myName}입니다.
      </h1>
      <button onClick = {changeName}>이름 바꾸기</button>
      <TestComponent title = {myName}></TestComponent>
    </div>*/


    // import React, { useState } from 'react';
    // import axios from 'axios';
    
    // const App = () => {
    //   const [file, setFile] = useState({});
    
    //   const imageUpload = e => {
    //     const imageTpye = e.target.files[0].type.includes('image');
    //     const videoTpye = e.target.files[0].type.includes('video');
    
    //     setFile({
    //       selectedFile: e.target.files[0],
    //       url: URL.createObjectURL(e.target.files[0]),
    //       image: imageTpye,
    //       video: videoTpye,
    //     });
    //     console.log(imageTpye);
    //   };
    
    //   const handlePost = async () => {
    //     const formData = new FormData(); //Form Data 만들어서 
    //     formData.append('file', file.selectedFile);  //file 담기
    //         //formData에 담아서 서버에 보내기
    //     const config = {
    //       header: { 'content-type': 'multipart/form-data' },
    //     }
    //     await axios.post("http://127.0.0.1:5000/fileupload", formData, config).then( //(업로드할 경로, 보낼 것)
    //        //127.0.0.1 local 컴퓨터 주소 5000 플라스크 기본 포트
    //       (response) => {
    //         if(response.data=="success"){
    //           console.log(response.data)
    //         }
    //         else{
    //           alert("비디오 업로드 실패")
    //         }
    //       }
    //     )
    //   }
    //   return (
    //     <div>
    //       <h1>1번</h1>
    //       <input type="file" onChange={imageUpload} />
    //       {file.image && <img src={file.url} />}
    //       {file.video && <video src={file.url} controls width="350px" />}
    //       <button onClick = {handlePost}>Submit</button>
    //     </div>
    //   );
    // };
    
    // export default App;

