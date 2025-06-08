const car = {type:"Fiat", model:500, color:"white"};
console.log(car);           //{ type: 'Fiat', model: '500', color: 'white' }
car.name = "Mustang";
console.log(car);           //{ type: 'Fiat', model: '500', color: 'white', name: 'Mustang' }
console.log(car.color);     // White
console.log(car["model"])   // 500


for (var i = 0; i > Object.keys(car).length; i++){
    console.log(i, car.i())
};

const PersonalData = {
    FirstName : "Routhu",
    LastName : "Dileep Kumar",
    MobileNumber : 8179724985
    }

PersonalData.FullName = PersonalData.FirstName + " " + PersonalData.LastName;
console.log(PersonalData)

//Create an Object
const person = {
  firstName:"John",
  lastName:"Doe",
  age:50, eyeColor:"blue"
};
console.log(person);

// Try to create a copy
const x = person;
console.log(person);
// This will change age in person:
x.age = 10;
console.log(person);

