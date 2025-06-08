function isPrime(num){
    if (num == 1){
        return false;
    }
    else if (num > 1){
        for (var i = 1; i < num/*(number(num**0.5)+1)*/; i++){
            console.log(i)
        }
    }
}

isPrime(5)

const iterable = ["Apple","Hello","Chinnu"];
for (let i of iterable) {
    console.log("i",i);
}


