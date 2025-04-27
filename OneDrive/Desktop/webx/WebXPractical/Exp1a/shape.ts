// Define the Shape interface with a method to calculate area
interface Shape {
    calculateArea(): number;
}

// Create Rectangle class that implements the Shape interface
class Rectangle implements Shape {
    // Properties
    private width: number;
    private height: number;
    
    // Constructor
    constructor(width: number, height: number) {
        this.width = width;
        this.height = height;
    }
    
    // Implement the calculateArea method required by the Shape interface
    calculateArea(): number {
        return this.width * this.height;
    }
    
    // Additional method specific to Rectangle
    displayDimensions(): void {
        console.log(`Width: ${this.width}, Height: ${this.height}`);
    }
}

// Create a Circle class that also implements Shape
class Circle implements Shape {
    // Property
    private radius: number;
    
    // Constructor
    constructor(radius: number) {
        this.radius = radius;
    }
    
    // Implement the calculateArea method required by the Shape interface
    calculateArea(): number {
        return Math.PI * this.radius * this.radius;
    }
}

// Example usage
const rectangle = new Rectangle(5, 10);
console.log(`Rectangle area: ${rectangle.calculateArea()}`);
rectangle.displayDimensions();

const circle = new Circle(7);
console.log(`Circle area: ${circle.calculateArea().toFixed(2)}`);
