import axios from "axios";

async function getCurTime(){
    var x = document.getElementById("myVideo");
    console.log(x.currentTime);
    // alert(x.currentTime);

    let data = JSON.stringify({
        time: x.currentTime,
    });

    //http://192.168.0.19:9091/time?id=
    return await axios.post("http://192.168.123.108:9091/time?id="+sessionStorage.getItem('id'), data, {headers:{"Content-Type" : "application/json"}})
    .then((response)=> {
        if(response.data === "success"){
            console.log(response.data)
        }
        else{
            alert("비디오 업로드 실패")
        }
    })

    // return axios({
    //     url: 'http://127.0.0.1:5000/time_flame',
    //     method: 'POST',
    //     data: {
    //         time: x.currentTime*1000,
    //     }
    // }).then(
    //     (response) => {
    //         if(response.data === "success"){
    //             console.log(response.data)
    //         }
    //         else{
    //             alert("시간 업로드 실패")
    //         }
    //     }
    // )
}
export default getCurTime;