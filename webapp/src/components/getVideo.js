import axios from "axios";

async function HandleOutput(){
        return await axios.get("http://172.16.166.231:9091/video?id="+sessionStorage.getItem('id'), {responseType: 'blob'}).then(
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