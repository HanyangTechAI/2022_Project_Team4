import React, {useState} from 'react';
import '../css/main5.css'

function Main5(){
    return(
        <div>
            <ul className = "main_changing">
                    <li>
                        <div><h1>비디오 변환중…</h1></div>
                        <div>
                            <h2>
                                잠시만 기다려주세요
                            </h2>
                        </div>
                        {/* <!—Progression Bar—> */}
                        <div></div>
                    </li>
                </ul>
        </div>
    );
}
export default Main5;