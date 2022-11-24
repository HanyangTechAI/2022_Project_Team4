import axios from "axios";
import {useState} from 'react'

async function GetImage(){
    const [file, setFile] = useState({
        preview_image: "",
    });

    // const config = {
    //     header: { 'content-type': 'multipart/form-data' },
    // }

    axios.get("http://127.0.0.1:5000/fileDownload/logo.jpg",{header: { 'content-type': 'multipart/form-data' },responseType: 'blob' })
    .then(res => {
        const myFile = new File([res.data], 'imageName')
        const reader = new FileReader()
        reader.onload = ev => {
            const previewImage = String(ev.target?.result)
            setFile({
            preview_image: previewImage,
            })
        }
        reader.readAsDataURL(myFile)
    
    })
    console.log(file.preview_image)
    return file.preview_image;
}
export default GetImage;

//고치기!!!!!!!!!!!!!!!!!!!!!!!!!!!!