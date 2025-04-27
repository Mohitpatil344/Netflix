// Base class with a method makeSound()
class Animal {
    makeSound(): void {
        console.log("Animal makes a sound");
    }
}

// Derived class that overrides the makeSound() method
class Dog extends Animal {
    makeSound(): void {
        console.log("Dog barks");
    }
}

// Create an instance of Dog and call makeSound()
const dog = new Dog();
dog.makeSound();

// Example of polymorphism - using a base class reference to call an overridden method
const animal: Animal = new Dog();
animal.makeSound(); // Still outputs "Dog barks"
