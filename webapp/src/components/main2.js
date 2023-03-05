import React, {useState} from 'react';
import "../css/main2.css"
import { Link, useLocation } from "react-router-dom";
import getCurTime from './getTime.js';

function Main2(){
    const location = useLocation();
    const [file, setFile] = useState({
        selectedFile: ([]),
        preview_URL: '',
        type: "video"
    });

    const fileReader = new FileReader();
    const selected = location.state.selectedFile;
    if (selected) {
        fileReader.readAsDataURL(selected)
    }
    
    fileReader.onload = () => {
        if(file.preview_URL !== fileReader.result){
            setFile({
                selectedFile: selected,
                preview_URL: fileReader.result,
                type: "video"
            });
        }
    }

    return(
        <div className = "wrap">
            <div className = "contents">
                비디오에서 삭제하고 싶은 사물 / 사람이 포함된 장면에서 멈춰주세요 !
            </div>
            <video className = "videoDisplay" id = "myVideo" controls={true} autoPlay={true} type = "video/mp4" src={file.preview_URL}/>
            {/* <button onClick = {getCurTime}type="button">Get current time position</button> */}
            <Link to ="/main2to3">
                <div onClick = {getCurTime} className = "selected">선택</div>
            </Link>
        </div>
    );
}
export default Main2;

// var x = document.getElementById("myVideo");
// console.log(x.currentTime);
// function getCurTime() { 
//     alert(x.currentTime);
// } 

// class Main2 extends Component{
//     constructor(props){
//         super(props);
//         this.state = {
//             selectedFile : props.selectedFile,
//             preview_URL: "",
//             type : "image"
//         };
//         const fileReader = new FileReader();
//         if (this.selectedFile) {
//             fileReader.readAsDataURL(this.selectedFile)
//         }
//         fileReader.onload = () => {
//             const fileType = this.selectedFile.type.split("/")[0];
//             let videoElement = document.createElement("video");
//             videoElement.src = fileReader.result;
//             this.setState({
//                 selectedFile: props.selectedFile,
//                 preview_URL: fileReader.result,
//                 type: fileType
//             });
//         }
//     }

//     render(){
//         return(
//             <div className = "wrap">
//                 <div className = "contents">
//                     비디오에서 삭제하고 싶은 사물 / 사람이 포함된 장면에서 멈춰주세요 !
//                 </div>
//                 <video className = "videoDisplay" controls={true} autoPlay={true} type = "video/mp4" src={this.state.preview_URL}/>
//                 <div className = "selected">
//                     선택
//                 </div>
//             </div>
//         )
//     }
// }

// export default Main2;
