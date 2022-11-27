import axios from "axios";
import {useState} from 'react'

async function GetImage(){
    const [file, setFile] = useState({
        preview_image: "",
    });

    // axios.get("http://172.16.166.231:9091/region?id="+sessionStorage.getItem('id')).then(
    //     (response)=> {
    //         console.log(response);
    //         const fileReader = new FileReader();
    //         fileReader.readAsDataURL(response.data)
    //         fileReader.onload = () => {
    //         const previewImage = response.data;
    //         setFile({
    //             preview_image: previewImage,
    //     })
    // }})


    // return file.preview_image;

    // const config = {
    //     header: { 'content-type': 'multipart/form-data' },
    // }
    //header는 받는 타입. 타입 설정.

    //http://127.0.0.1:5000까지가 서버, 서버에 /fileDownload 이런 요청을 보내면 서버에서 /fileDownload 처리하는 부분이 있어야함.
    //query(? 이렇게)로 video id 요청. /fileDownload/ 요부분 image, video에 따라서 다 다르게 바꿔가면서. 
    // axios.get("http://127.0.0.1:5000/fileDownload/"+"",{header: { "Content-Type" : "application/json" } })
    // .then(res => {
    //     const myFile = new File([res.data], 'imageName')
    //     const reader = new FileReader()
    //     reader.onload = ev => {
    //         const previewImage = String(ev.target?.result)
    //         setFile({
    //         preview_image: previewImage,
    //         })
    //     }
    //     reader.readAsDataURL(myFile)
    
    // })
    // console.log(file.preview_image)
    // return file.preview_image;

    
}
export default GetImage;

//고치기!!!!!!!!!!!!!!!!!!!!!!!!!!!!