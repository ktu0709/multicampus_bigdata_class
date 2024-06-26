let $ = function(cssSelector, message){
    let htmlElements = document.querySelectorAll(cssSelector);

    if(message){
               htmlElements.forEach(e => {e.innerHTML += message + '<br>'});
            }

            if(htmlElements.length == 1) return htmlElements[0];
            return htmlElements;
     }

      class Person{

            // public field
            name;

            // private field, #
            #gender;

            // static 변수
            // 자바스크립트의 static은 자바와 달리 오직 type으로만 static 속성을 다룰 수 있다.
            // Person.species (o), hmd.species(x)
            static species = 'mammalia';

            // 상수
            // 속성명을 대문자로 작성하면 상수로 간주. 실제로 상수가 되는 것(x), 개발자들 끼리의 약속
            // 자바스크립의 내장객체에서도 사용되고 있는 방식
            #HABITAT ='earth';



            // 생성자
            constructor(name, gender){
                this.name = name;
                this.#gender = gender;
            }

            // setter
            set gender(v){
                console.dir('setGender 호출됨')
                this.#gender = v;
            }

            // getter
            get gender(){
                console.dir('getGender 호출됨')
                return this.#gender;
            }

            get HABITAT(){
                console.dir('getHABITAT 호출됨')
                return this.#HABITAT;
            }

        }

        let hmd = new Person('홍길동', '남');
        hmd.gender = 'male';
        console.dir(hmd);
        $('#classNote', hmd.name);
        $('#classNote', hmd.gender);
        $('#classNote', Person.species);
        $('#classNote', hmd.HABITAT);

        console.dir(hmd);


        //상속
        class Student extends Person{

            #arcademy;

            constructor(name, gender, arcademy){
                // 부모의 생성자를 먼저 호출해야 한다.
                super(name, gender);
                this.#arcademy = arcademy;
            }

            set arcademy(v){
                this.#arcademy = v;
            }

            get arcademy(){
                return this.#arcademy;
            }
        }

        $('#classNote', '---------------------------------------');

        let hgd = new Student('홍길동', '남', 'MC');
        $('#classNote', hgd.name);
        $('#classNote', hgd.gender);
        $('#classNote', Person.species);
        $('#classNote', hgd.HABITAT);
        $('#classNote', hgd.arcademy);
        console.dir(hgd);

        // hgd.#arcademy = 'a';
        // console.dir(hgd.#arcademy);