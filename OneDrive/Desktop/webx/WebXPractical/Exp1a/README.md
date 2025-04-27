# TypeScript Experiment - Exp2

This experiment demonstrates basic concepts of TypeScript including classes, interfaces, and type annotations.

## Prerequisites

1. Node.js and npm installed on your system
2. TypeScript installed globally or locally
   ```
   npm install -g typescript
   ```

## Running the Examples

Each TypeScript file can be compiled and run using the following steps:

1. **Compile TypeScript to JavaScript**:
   ```
   tsc filename.ts
   ```
   This will generate a JavaScript file with the same name.

2. **Run the JavaScript file with Node.js**:
   ```
   node filename.js
   ```

## Examples Included

### Example 1: Classes and Inheritance
- File: `inheritance.ts`
- This example demonstrates class inheritance in TypeScript with a base Animal class and a derived Dog class.
- Run:
  ```
  tsc inheritance.ts
  node inheritance.js
  ```

### Example 2: Access Modifiers
- File: `accessModifiers.ts`
- This example shows the use of public, private, and protected access modifiers in TypeScript.
- Run:
  ```
  tsc accessModifiers.ts
  node accessModifiers.js
  ```

### Example 3: Interfaces
- File: `interfaces.ts`
- This example demonstrates interfaces in TypeScript with a Shape interface.
- Run:
  ```
  tsc interfaces.ts
  node interfaces.js
  ```

### Example 4: Types and Type Inference
- File: `types.ts`
- This example shows TypeScript's type system and type inference.
- Run:
  ```
  tsc types.ts
  node types.js
  ```

## Setting Up a New TypeScript Project

If you want to create a new TypeScript project from scratch:

1. Create a new directory and navigate to it:
   ```
   mkdir my-typescript-project
   cd my-typescript-project
   ```

2. Initialize a new npm project:
   ```
   npm init -y
   ```

3. Install TypeScript locally:
   ```
   npm install typescript --save-dev
   ```

4. Create a TypeScript configuration file:
   ```
   npx tsc --init
   ```

5. Create your TypeScript files and compile using:
   ```
   npx tsc
   ```

## Notes

- TypeScript files use the `.ts` extension
- Compiled JavaScript files use the `.js` extension
- The TypeScript compiler (`tsc`) converts TypeScript code to JavaScript
- Node.js is used to run the compiled JavaScript code 