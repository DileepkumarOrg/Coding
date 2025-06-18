function changeColor() {
  const colors = ["#FF5733", "#33FF57", "#3357FF", "#F39C12", "#9B59B6", "#1ABC9C"];
  const randomColor = colors[Math.floor(Math.random() * colors.length)];
  document.body.style.backgroundColor = randomColor;
}

function calculateSum() {
  const num1 = document.getElementById("num1").value;
  const num2 = document.getElementById("num2").value;
  const sum = Number(num1) + Number(num2);
  document.getElementById("result").innerText = "Result: " + sum;
}

function Math(){
    const Num1 = Number(document.getElementById("Num1").value);
    const Num2 = Number(document.getElementById("Num2").value);
    const Sym = document.getElementById("Sym").value;
    let result;
    switch (Sym){
        case "+":
            result = Num1 + Num2;
            break;
        case "-":
            result = Num1 - Num2;
            break;
        case "/":
            result = Num1 / Num2;
            break;
        case "*":
            result = Num1 * Num2;
            break;
        case "%":
            result = Num1 % Num2;
            break;
        default:
            result = 0;
            break;
    }
    document.getElementById("result1").innerText = "Result : " + result;
}

function CalculateAge(){
    const dob = Date(document.getElementById("dob").value);
    const today = Date(document.getElementById("today").value);
    var result2 = today-dob;
    document.getElementById("result2").innerText = "Result : "+ result2;
}