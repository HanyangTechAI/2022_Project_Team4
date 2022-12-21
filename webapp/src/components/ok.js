import axios from 'axios'

async function Ok(){
    let data = JSON.stringify({
        isConfirmed: true,
    });

    //http://192.168.0.19:9091/time?id=
    return await axios.post("https://3c69-112-156-88-200.jp.ngrok.io/mask?id="+sessionStorage.getItem('id'), data, {headers:{"Content-Type" : "application/json"}})
    .then((response)=> {
        if(response.data === "success"){
            console.log(response.data)
        }
        else{
            alert("비디오 업로드 실패")
        }
    })
}

export default Ok;