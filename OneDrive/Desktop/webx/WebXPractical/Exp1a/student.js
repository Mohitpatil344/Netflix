var Student = /** @class */ (function () {
    // Constructor to initialize the properties
    function Student(name, rollNo, course) {
        this.name = name;
        this.rollNo = rollNo;
        this.course = course;
    }
    // Method to display all properties
    Student.prototype.displayDetails = function () {
        console.log("Name: ".concat(this.name));
        console.log("Roll No: ".concat(this.rollNo));
        console.log("Course: ".concat(this.course));
    };
    // Method to demonstrate private property access
    Student.prototype.updateRollNo = function (newRollNo) {
        this.rollNo = newRollNo;
        console.log("Roll No updated to: ".concat(this.rollNo));
    };
    return Student;
}());
// Example usage
var student = new Student("John Doe", 101, "Computer Science");
student.displayDetails();
// Public property can be accessed directly
console.log("\nAccessing public property: ".concat(student.name));
// Private property cannot be accessed directly
// Uncommenting the line below would cause a compilation error
// console.log(student.rollNo);
// Protected property cannot be accessed directly from outside the class
// Uncommenting the line below would cause a compilation error
// console.log(student.course);
// But we can update the private property using a class method
student.updateRollNo(102);
student.displayDetails();
