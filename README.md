# Genetic Algorithm for Job Shop Scheduling Optimization

## 🌟 Project Overview

Welcome to the GitHub repository for the AI-Driven Job Shop Scheduling System! This project was developed as part of the ENCS 3340 Artificial Intelligence course at the Faculty of Engineering and Technology. Utilizing a Genetic Algorithm, this system optimizes the scheduling of operations in a manufacturing plant, ensuring that each product is processed in the most efficient sequence possible to minimize overall production time.


## Components

### Process Class
The `Process` class represents an individual job process, containing information such as job number, machine number, sequence number, duration, and start time. It provides methods for string representations and equality checks.

### Chromosome Class
The `Chromosome` class simulates a possible scheduling solution, holding a list of `Process` instances for each machine. It supports methods to add processes, compare chromosomes based on their evaluation (fitness), and generate a schedule based on process dependencies and machine availability.

## ⚡ Algorithm Features
- **Initial Population:** Randomly generated valid solutions represented by chromosomes.
- **Fitness Calculation:** Evaluates chromosomes based on the sum of job completion times.
- **Genetic Operations:** Includes selection via Roulette Wheel, crossover, and mutation to evolve the population towards optimal solutions.
- **Termination:** Stops when no improvement is observed over a set number of generations.

## ⚙️ Technologies Used
- **Python**: Core programming language for developing the scheduling algorithm and managing input/output operations.
- **Matplotlib**: Used for generating Gantt charts that visually represent the scheduling results.
- 

## Usage
- **Setup:** Define the number of machines and jobs, and initialize the genetic algorithm parameters.
- **Input:** Load job and machine data from user input or a CSV file.
- **Execution:** Run the genetic algorithm to generate optimized job scheduling.
- **Visualization:** View the scheduling results as a Gantt chart.


## 🌱 What's Next

- **Exploring Alternative Fitness Functions**: I am investigating different fitness functions to enhance the algorithm's accuracy and efficiency.
- **Code Enhancements**: Plans are underway to improve the codebase, focusing on streamlining both input and output processes to make the system more user-friendly and adaptable to various manufacturing settings.

## 📖 Further Reading

For a more detailed discussion on problem formulation and the test cases used to evaluate this system, please refer to the [report attached](https://github.com/SarahYousefH/AI-Job-Scheduling-Program/blob/b0fb34a4b63c022411e951cd7f269172323c6343/Report_AI_Project.pdf).


