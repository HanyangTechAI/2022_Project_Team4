import React, {Component} from 'react';
import axios from 'axios';
import default_image from "../images/default_image.png"
import folder_img from '../images/folderIcon.png'
import '../css/main1.css'
import { Link } from "react-router-dom"

// function onClickUpload() {
//         let myInput = document.getElementById("file-input");
//         myInput.click();
//     }

class Main1 extends Component{
    constructor(props){
        super(props);
        this.state = {
            selectedFile : ([]),
            preview_URL: {default_image},
            type: "image"
        };
        this.handlePost = this.handlePost.bind(this);
    }
    // handleFileInput(e){
    //     this.setState({selectedFile : e.target.files[0],}); //file 하나만 받으니까 index 0으로
    // }

    saveImage(e){
        e.preventDefault();
        const fileReader = new FileReader();
        if (e.target.files[0]) {
            fileReader.readAsDataURL(e.target.files[0])
        }
        fileReader.onload = () => {
            const fileType = e.target.files[0].type.split("/")[0];
            let videoElement = document.createElement("video");
            videoElement.src = fileReader.result;
            this.setState({
                selectedFile: e.target.files[0],
                preview_URL: fileReader.result,
                type: fileType
            });
        }
    }
    deleteImage = () =>{
        this.setState = {
            selectedFile : [],
            preview_URL: {default_image},
            type: "image"
        };
    }
    async handlePost(){
        const formData = new FormData(); //Form Data 만들어서 
        formData.append('file', this.state.selectedFile);  //file 담기
        //formData에 담아서 서버에 보내기
        const config = {
            header: { 'content-type': 'multipart/form-data' },
        }

        //http://192.168.0.19:9091/upload
        return axios.post("http://192.168.123.107:9091/upload", formData, config).then( //(업로드할 경로, 보낼 것)
        //127.0.0.1 local 컴퓨터 주소 5000 플라스크 기본 포트
            (response) => {
                // if(response.data === "SUCCESS"){
                //     // console.log(response.data); // sessionStorage.setItem('id', response.data);로 바꾸기
                //     // sessionStorage.setItem('test', 'hello'); // response.data는 string type이어야함. return type string.
                //     // console.log(sessionStorage.getItem('test'));
                //     console.log("success!!!!!!")
                // }
                // else{
                //     alert("비디오 업로드 실패")
                // }

                if(response.status===200){ //성공하면 페이지 이동하게 구현하기
                    sessionStorage.setItem('id', response.data);
                    console.log(sessionStorage.getItem('id'));
                }
            }
        )
    }
    render(){
        return(
            <div>
                <input type = "file" id = "input-file" hidden accept = "video/mp4"  onChange = {e => this.saveImage(e)}/>
                <Link to = '/main2' state={{ selectedFile: this.state.selectedFile }}>
                {/* state={{ selectedFile: this.state.selectedFile }} */}
                    <button onClick = {this.handlePost} id = "button-click" hidden>Submit</button>
                </Link>
                <ul className = "main_texts">
                    <li>
                        <div><h1>Video Inpainting</h1></div>
                        <div>
                            <h2>
                                비디오에서 원하지 않는 사물 / 사람을 삭제하세요 !
                            </h2>
                        </div>
                        <div className="file-wrapper">
                            <video controls={true} autoPlay={true} type = "video/mp4" src={this.state.preview_URL}/>
                        </div>
                        <div className='buttons'>
                            <div>
                                <label htmlFor ="input-file">
                                    <form className = "select_button">
                                        <ul className = "icons">
                                            <li>
                                            {/* <input type = "file" id = "file-input" hidden/> */}
                                                <div className = "select_video">비디오 선택하기</div>
                                                <div className = "folder_img">
                                                    <img src = {folder_img}/>
                                                </div>
                                            </li>
                                        </ul>
                                    </form>
                                </label>
                            </div>
                            <div>
                                <label htmlFor='button-click'>
                                    <div className = "submit">완료</div>
                                </label>
                            </div>
                        </div>
                    </li>
                </ul>
                {/* id = "button-click" */}
                {/* <button onClick = {this.handleOutput()}>Download</button> */}
            </div>
        )
    }
}
export default Main1;