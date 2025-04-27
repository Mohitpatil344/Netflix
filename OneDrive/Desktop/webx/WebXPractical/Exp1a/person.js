// Create Person class that implements the PersonInfo interface
var Person = /** @class */ (function () {
    // Constructor to initialize the properties
    function Person(name, age, email) {
        this.name = name;
        this.age = age;
        this.email = email;
    }
    // Method to display person information
    Person.prototype.displayInfo = function () {
        console.log("Name: ".concat(this.name));
        console.log("Age: ".concat(this.age));
        if (this.email) {
            console.log("Email: ".concat(this.email));
        }
    };
    // Method to check if person is an adult
    Person.prototype.isAdult = function () {
        return this.age >= 18;
    };
    return Person;
}());
// Example usage
var person1 = new Person("Alice Smith", 25, "alice@example.com");
person1.displayInfo();
console.log("Is adult: ".concat(person1.isAdult()));
var person2 = new Person("Bob Johnson", 16);
person2.displayInfo();
console.log("Is adult: ".concat(person2.isAdult()));
