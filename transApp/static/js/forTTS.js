const button2 = document.getElementById("translateText");
const translateUrl = 'http://127.0.0.1:8000/translate'

const gettranslateText = function() {
  var originalText = document.getElementById('msg').value; // 원본 텍스트 가져오기

  axios.get(translateUrl,{
    //withCredentials: true,
    params:{
      source: 'ko',
      target: 'en',
      text: originalText
    }
}).then(
    (response) => {
      var translation = response.data.message.result.translatedText;
      var translatedTextContainer = document.getElementById('translated-text-container');
      translatedTextContainer.textContent = translation;
  }).catch(function(error) {
    console.log('Error:', error);
  });
}
// 번역하기 버튼에 클릭 이벤트 처리기 추가
const translateButton = document.getElementById('translateText');
translateButton.addEventListener('click', gettranslateText);