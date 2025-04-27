// Create Rectangle class that implements the Shape interface
var Rectangle = /** @class */ (function () {
    // Constructor
    function Rectangle(width, height) {
        this.width = width;
        this.height = height;
    }
    // Implement the calculateArea method required by the Shape interface
    Rectangle.prototype.calculateArea = function () {
        return this.width * this.height;
    };
    // Additional method specific to Rectangle
    Rectangle.prototype.displayDimensions = function () {
        console.log("Width: ".concat(this.width, ", Height: ").concat(this.height));
    };
    return Rectangle;
}());
// Create a Circle class that also implements Shape
var Circle = /** @class */ (function () {
    // Constructor
    function Circle(radius) {
        this.radius = radius;
    }
    // Implement the calculateArea method required by the Shape interface
    Circle.prototype.calculateArea = function () {
        return Math.PI * this.radius * this.radius;
    };
    return Circle;
}());
// Example usage
var rectangle = new Rectangle(5, 10);
console.log("Rectangle area: ".concat(rectangle.calculateArea()));
rectangle.displayDimensions();
var circle = new Circle(7);
console.log("Circle area: ".concat(circle.calculateArea().toFixed(2)));
