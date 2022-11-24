import React, { Component } from 'react';
import '../css/footer.css'

class Footer extends Component{
    render(){
        return(
            <footer id = "link_contact">
                <div>
                    HAI Team 4
                    <div>Addr. 서울특별시 성동구 한양대학교 ITBT관</div>
                    <div>02-123-456-7</div>
                </div>
                <div>
                    COPYRIGHT HAI Team 4 All Rights Reserved
                </div>
            </footer>
        );
    }
}

export default Footer;