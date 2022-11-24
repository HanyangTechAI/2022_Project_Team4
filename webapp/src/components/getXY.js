import axios from "axios";

async function GetXY(e) {
    var coordinateX = ((e.nativeEvent.offsetX ) / 900) * 100;
    var coordinateY = ((e.nativeEvent.offsetY ) / 570) *100;
    console.log(coordinateX);
    console.log(coordinateY);

    let data = JSON.stringify({
        coordinateX : coordinateX,
        coordinateY : coordinateY,
    });
    return axios.post("http://127.0.0.1:5000/getXY", data, {headers:{"Content-Type" : "application/json"}})
    .then((response)=> {
        if(response.data === "success"){
            console.log(response.data)
        }
        else{
            alert("비디오 업로드 실패")
        }
    })
}
export default GetXY;