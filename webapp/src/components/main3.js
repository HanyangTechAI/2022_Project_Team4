import React, {useState, useEffect} from 'react';
import '../css/main2.css';
import { Link } from 'react-router-dom';
import GetXY from './getXY.js';

function Main3(props){
    const [file, setFile] = useState({
        preview_image: props.image,
    });

    // useEffect(() => {
    //     axios.get("http://192.168.123.108:9091/region?id="+sessionStorage.getItem('id'), {responseType: 'blob'}).then(
    //     (response)=> {
    //         console.log(response);
    //         console.log(response.data);
    //         const fileReader = new FileReader();
    //         fileReader.readAsDataURL(response.data)
    //         fileReader.onload = () => {
    //         const previewImage = fileReader.result;
    //         console.log(previewImage);
    //         setFile({
    //             preview_image: previewImage,
    //     })
    // }})
    // },[]);
    // axios.get<Blob>( "http://172.16.166.231:9091/region?id="+sessionStorage.getItem('id'), { headers: {}, responseType: 'blob' }).then(res => {
    //     const myFile = new File([res.data], 'imageName')
    //     console.log(myFile)
        // const reader = new FileReader()
        // reader.onload = () => {
        //   const previewImage = String(ev.target?.result)
        //   setFile(previewImage) // myImage라는 state에 저장했음
        //   }
        // reader.readAsDataURL(myFile)
    // })

    // for(var i = 0; i < 1; i++){
    //     setFile({
    //         preview_image: {GetImage}
    //     })
    // }


    // let data = JSON.stringify({
    //     hihi: 3,
    // });

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

    //http://192.168.0.19:9091/region?id=
    // if(file.preview_image == default_image){ //이거 if문 안돌아간다..왜
    //     axios.post("http://172.16.166.231:9091/region?id="+sessionStorage.getItem('id'), data, {headers:{"Content-Type" : "application/json"}}).then(
    //     (response)=> {
    //         const fileReader = new FileReader();
    //         fileReader.readAsDataURL(response.data);
    //         fileReader.onload = () => {
    //         // const previewImage = response.data;
    //         setFile({
    //             preview_image: fileReader.result,
    //         })
    //     }
    // })
    //만약에 url로 받으면, 그냥 url로 setFile해버리고 그거 그냥 src에 넣기

    // }
    // let binarySrc = file.preview_image;
    // document.getElementById("test").src = "data:image/png;base64," + binarySrc;
    // coordinateX: '', //사용자 마우스 클릭한 좌표 저장
    // coordinateY: '',

    // const imageOverlay = e => { 
    // setFile(prev => ({
    // ...prev,
    // preview_image: {default_image},
    // coordinateX:
    //   ((e.nativeEvent.offsetX ) / 900) * 100, // 가로가 900이라..
    // coordinateY:
    //   ((e.nativeEvent.offsetY ) / 570) *100, // 세로가 570이라..
    // }));
    // };
    // console.log(file.coordinateX);
    // console.log(file.coordinateY);

    return(
        <div>
            <div className = "contents">
                비디오에서 삭제하고 싶은 사물 / 사람의 누끼를 골라주세요 !
            </div>
            <Link to='/main3to4'>
                <div>
                    <img className='preview_image' src = {file.preview_image} onClick= {e=>{GetXY(e)}}/>
                </div>
            </Link>
            {/* <Link to = "/main4">
                <div className = "selected">
                    완료
                </div>
            </Link> */}
        </div>
    );
}
export default Main3;