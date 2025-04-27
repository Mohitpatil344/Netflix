var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
// Base class with a method makeSound()
var Animal = /** @class */ (function () {
    function Animal() {
    }
    Animal.prototype.makeSound = function () {
        console.log("Animal makes a sound");
    };
    return Animal;
}());
// Derived class that overrides the makeSound() method
var Dog = /** @class */ (function (_super) {
    __extends(Dog, _super);
    function Dog() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Dog.prototype.makeSound = function () {
        console.log("Dog barks");
    };
    return Dog;
}(Animal));
// Create an instance of Dog and call makeSound()
var dog = new Dog();
dog.makeSound();
// Example of polymorphism - using a base class reference to call an overridden method
var animal = new Dog();
animal.makeSound(); // Still outputs "Dog barks"
