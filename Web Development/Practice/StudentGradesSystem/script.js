function markGrade(){
    const Englishmarks = Number(document.getElementById("English").value);
    const Hindhimarks = Number(document.getElementById("Hindhi").value);
    const Mathsmarks = Number(document.getElementById("Maths").value);
    const Sciencemarks = Number(document.getElementById("Science").value);
    const Socialmarks = Number(document.getElementById("Social").value);
    var marks = (Englishmarks + Hindhimarks + Mathsmarks + Sciencemarks + Socialmarks) / 5;
    switch(true){
        case marks >= 90 :
            result = "A+ Grade";
            break;
        case marks >= 80:
            result = "A Grade";
            break;
        case marks >= 70 :
            result = "B Grade";
            break;
        case marks >= 60:
            result = "C Grade";
            break;
        case marks >= 50 :
            result = "D Grade";
            break;
        case marks >= 40:
            result = "E Grade";
            break;
        case marks < 40:
            result = "Fail";
            break;
        default:
            result = "None";
            break;
    };

    document.getElementById("grade").innerText = "Result : "+ result;
}

