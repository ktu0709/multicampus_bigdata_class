class Sung {
  constructor(my_name, kor, eng, mat) {
    this.my_name = my_name;
    this.kor = kor;
    this.eng = eng;
    this.mat = mat;
  }

  calculateTotal() {
    return this.kor + this.eng + this.mat;
  }

  calculateAverage() {
    return this.calculateTotal() / 3;
  }

  printScore() {
    const total = this.calculateTotal();
    const average = this.calculateAverage();

    const scoreContainer = document.getElementById("scoreContainer");

      const scoreText = `${this.my_name}'s Total: ${total}, Average: ${average}`;
      const scoreParagraph = document.createElement("p");
      scoreParagraph.textContent = scoreText;

    scoreContainer.appendChild(scoreParagraph);
  }
}
/////////////////////////////////////////////////////////
//1.폼의 id를 찾아서  scoreForm 으로 대입 
const scoreForm = document.getElementById("scoreForm");
//2. 폼의 이벤트를 추가 한다.  "submit"이라는 글자를 받아오면  
// 3. 함수핸들링 한다.  
// ex) scoreForm.addEventListener("submit", function (event) {}) 

scoreForm.addEventListener("submit", function (event) {
  event.preventDefault();

  ////////폼의 입력상자 에서 받은 값들을 각각의 변수에 대입한다. 
  const nameInput = document.getElementById("name"); // 폼의 입력상자 
  const korInput = document.getElementById("kor");//폼의 입력상자 
  const engInput = document.getElementById("eng");//폼의 입력상자 
  const matInput = document.getElementById("mat");//폼의 입력상자 

  ////////각각의 변수에 대입
  const name = nameInput.value;
  const kor = Number(korInput.value);  // 90 '90' Number를 통해 수치로 변환  
  const eng = Number(engInput.value);
  const mat = Number(matInput.value);

  const student = new Sung(name, kor, eng, mat);
  student.printScore();

  // Reset form inputs
  scoreForm.reset();
});
