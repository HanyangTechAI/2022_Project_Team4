import axios from "axios";

async function HandleOutput(){
    //파일 다운로드 요청 API, responseType: 받아올 데이터 타입 정하기. blob = binary Large Object 큰 데이터들 다룰 때 사용. 이미지, 오디오, 영상 등
        return await axios.get("https://3c69-112-156-88-200.jp.ngrok.io/video?id="+sessionStorage.getItem('id'), {responseType: 'blob'}).then(
        (response)=> {
            console.log(response.data);
            const blob = new Blob([response.data], {type: 'video/mp4'}); //전달 받은 데이터를 blob으로 변환
            const fileObjectUrl = window.URL.createObjectURL(blob);
    
            const link = document.createElement("a");
            link.href = fileObjectUrl;
            link.style.display = "none";
    
            link.download = sessionStorage.getItem('id');
            //"download_Success";
            document.body.appendChild(link);
            link.click();
            link.remove();
    
            window.URL.revokeObjectURL(fileObjectUrl);
        });
}
export default HandleOutput;