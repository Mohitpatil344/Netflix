class Student {
    // Public property - accessible from anywhere
    public name: string;
    
    // Private property - only accessible within this class
    private rollNo: number;
    
    // Protected property - accessible within this class and derived classes
    protected course: string;
    
    // Constructor to initialize the properties
    constructor(name: string, rollNo: number, course: string) {
        this.name = name;
        this.rollNo = rollNo;
        this.course = course;
    }
    
    // Method to display all properties
    displayDetails(): void {
        console.log(`Name: ${this.name}`);
        console.log(`Roll No: ${this.rollNo}`);
        console.log(`Course: ${this.course}`);
    }
    
    // Method to demonstrate private property access
    updateRollNo(newRollNo: number): void {
        this.rollNo = newRollNo;
        console.log(`Roll No updated to: ${this.rollNo}`);
    }
}

// Example usage
const student = new Student("John Doe", 101, "Computer Science");
student.displayDetails();

// Public property can be accessed directly
console.log(`\nAccessing public property: ${student.name}`);

// Private property cannot be accessed directly
// Uncommenting the line below would cause a compilation error
// console.log(student.rollNo);

// Protected property cannot be accessed directly from outside the class
// Uncommenting the line below would cause a compilation error
// console.log(student.course);

// But we can update the private property using a class method
student.updateRollNo(102);
student.displayDetails();
