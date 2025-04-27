// Define the PersonInfo interface with required properties
interface PersonInfo {
    name: string;
    age: number;
}

// Create Person class that implements the PersonInfo interface
class Person implements PersonInfo {
    // Properties required by the interface
    name: string;
    age: number;
    
    // Additional property not in the interface
    email?: string; // Optional property
    
    // Constructor to initialize the properties
    constructor(name: string, age: number, email?: string) {
        this.name = name;
        this.age = age;
        this.email = email;
    }
    
    // Method to display person information
    displayInfo(): void {
        console.log(`Name: ${this.name}`);
        console.log(`Age: ${this.age}`);
        if (this.email) {
            console.log(`Email: ${this.email}`);
        }
    }
    
    // Method to check if person is an adult
    isAdult(): boolean {
        return this.age >= 18;
    }
}

// Example usage
const person1 = new Person("Alice Smith", 25, "alice@example.com");
person1.displayInfo();
console.log(`Is adult: ${person1.isAdult()}`);

const person2 = new Person("Bob Johnson", 16);
person2.displayInfo();
console.log(`Is adult: ${person2.isAdult()}`);
