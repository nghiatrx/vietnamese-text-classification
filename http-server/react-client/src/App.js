import React, { Component } from 'react';
import './App.css';

const samples = [
  'Range Rover Evoque thế hệ mới đổi thiết kế, giá từ 40.700 USD Phiên bản máy dầu tiêu chuẩn có giá rẻ nhất từ 40.700 USD, xe thay đổi một số chi tiết ở ngoại thất và nội thất. Land Rover đã công bố thế hệ thứ 2 dòng xe Evoque, sau khi đời đầu lên kệ hơn 7 năm. Thiết kế Range Rover Evoque 2020 có nhiều nét quen thuộc so với thế hệ đang bán, nhưng hãng xe Anh đã loại đi khá nhiều yếu tố thể thao. Phần đầu xe có cụm đèn mỏng thời thượng, lưới tản nhiệt nhỏ. Tuỳ vào cấu hình, Evoque 2020 sẽ có hốc gió lớn, tương tự như phiên bản cũ. Nhìn ngang thân xe kiểu dáng của Evoque mới vẫn dễ nhận diện, tuy nhiên một số điểm ở thiết kế có bóng dáng của Velar như hệ thống đèn. Kiểu dáng xe được giới truyền thống quốc tế đánh giá cao hơn so với Volvo XC40 hay Audi Q3. Phía đuôi xe không thay đổi nhiều với hiện tại, ngoại trừ cụm đèn hậu nhỏ giống Velar.',
  'Mazda2 New lần đầu sở hữu công nghệ kiểm soát gia tốc Công nghệ kiểm soát gia tốc G-Vectoring Control (GVC) giúp xe vận hành ổn định, tăng mức an toàn và thoải mái cho tất cả người ngồi trên xe. Dù chưa chính thức ra mắt tại Việt Nam, Mazda2 phiên bản mới đã được nhiều khách hàng quan tâm và chú ý nhờ được trang bị công nghệ tiên tiến. Nổi bật là công nghệ GVC, mang đến sự ổn định và thoải mái cho người sử dụng trong suốt hành trình. ',
  'Phiên bản màu trắng của Galaxy Note9 được Samsung giới thiệu tại Đài Loan có duy nhất bộ nhớ 128 GB và bán với giá 999 USD, đắt ngang iPhone XS 64 GB. Máy lên kệ từ đầu tháng 12 để đón đầu mùa Giáng sinh. ',
  '10 bệnh viện tốt nhất thế giới Các bệnh viện được đánh giá bởi đội ngũ bác sĩ giỏi chuyên môn, thái độ phục vụ tận tâm và thiết bị chữa bệnh hiện đại.',
  'Tối qua, đôi tuyển Việt Nam đã giành chiến thắng với tỷ số 3-0 trước Campuchia và giành ngôi đầu bảng A. Ấn tượng hơn khi chúng ta chưa để thủng lưới bàn nào sau 4 trận đấu đã qua.'
]

class App extends Component {
  state = {
    content: '',
    result: [],
    classes: [],
    maxPos: 0
  }
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <div style={{fontSize: '19px'}}>
            Vietnamese text classification, you can copy the articles from vnexpress.net, news.zing.vn, dantri.com.vn and paste it here
          </div>

          {
            this.state.classes.length > 0 && (
              <p>Total Classes { this.state.classes.length }</p>
            )
          }
        
          <div>
            <a style={{color: '#fff'}} href='https://github.com/nghiatrx/vietnamese-text-classification/'>
              Github
            </a>
          </div>

          <div>
            <textarea
              className='Text-Content'
              rows="15" 
              cols="100"
              placeholder='Content'
              onChange={e => {
                this.setState({
                  content: e.target.value
                })
              }}
              value={this.state.content} />
          </div>
          
          <div>
            <button className='Send-Btn' onClick={() => {
              const i = Math.floor(Math.random() * samples.length)
              this.setState({
                content: samples[i]
              })
            }}>
              Get sample
            </button>
          </div>
              
          <div>
            <button className='Send-Btn' onClick={() => {
              fetch('http://127.0.0.1:5000', {
                method: 'post',
                headers: {'Content-Type':'application/json'},
                body: JSON.stringify({ 'content': this.state.content })
               })
               .then(async response => {
                  const json = await response.json()
                  let max = 0
                  let maxPos = 0
                  json.result.forEach((i, index) => {
                    if (i > max) {
                      max = i
                      maxPos = index
                    }
                  })
                  this.setState({
                    result: json.result,
                    classes: json.classes,
                    maxPos
                  })
               })
            }}>Send</button>
          </div>

          {
            this.state.result.length > 0 && (
              <div>
                <p>
                  Predict: <b>{ this.state.classes[this.state.maxPos] }</b>
                </p>
              </div>
            )
          }
          
          <div>
            <ul className='result'>
              {
                this.state.classes.map((i, index) => (
                  <li key={index} className={this.state.maxPos === index ? 'maxValue' : ''}>
                    { i } - { (this.state.result[index] * 100).toFixed(2) } %
                  </li>
                ))
              }
            </ul>
          </div>
        </header>
      </div>
    );
  }
}

export default App;
