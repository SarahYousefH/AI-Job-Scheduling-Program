# Genetic Algorithm for Job Shop Scheduling Optimization

## Introduction
This project implements a genetic algorithm to optimize job shop scheduling. The focus is on efficiently scheduling jobs on machines with specific constraints and sequences, minimizing overall job completion times.

## Project Details
- **Course:** ENCS 3340 Artificial Intelligence
- **Student:** Sarah Hassouneh
- **Instructor:** Dr. Yazan Abu Farha
- **Date:** May 18, 2024

## Components

### Process Class
The `Process` class represents an individual job process, containing information such as job number, machine number, sequence number, duration, and start time. It provides methods for string representations and equality checks.

### Chromosome Class
The `Chromosome` class simulates a possible scheduling solution, holding a list of `Process` instances for each machine. It supports methods to add processes, compare chromosomes based on their evaluation (fitness), and generate a schedule based on process dependencies and machine availability.

## Algorithm Features
- **Initial Population:** Randomly generated valid solutions represented by chromosomes.
- **Fitness Calculation:** Evaluates chromosomes based on the sum of job completion times.
- **Genetic Operations:** Includes selection via Roulette Wheel, crossover, and mutation to evolve the population towards optimal solutions.
- **Termination:** Stops when no improvement is observed over a set number of generations.

## Usage
The genetic algorithm is encapsulated in classes that manage the job shop scheduling scenario. Users can instantiate the `Chromosome` class, populate it with `Process` instances, and execute the algorithm to find optimized schedules.

## Conclusion
This project demonstrates the application of genetic algorithms in complex scheduling scenarios, showing significant potential for operational efficiency improvements in manufacturing and other sectors requiring precise job scheduling.


# Genetic Algorithm for Job Shop Scheduling Optimization

## Introduction
This project utilizes a genetic algorithm to optimize job scheduling across multiple machines in a manufacturing setup. The goal is to minimize the total job completion time while adhering to machine constraints and job sequences.

## Features
- **Process and Chromosome Classes:** Define job processes and potential scheduling solutions.
- **Dynamic Input Handling:** Supports input through hardcoded strings or CSV files, allowing for flexible testing scenarios.
- **Genetic Operations:** Implements selection, crossover, and mutation to evolve the population towards optimal solutions.
- **Gantt Chart Visualization:** Uses Matplotlib to visualize the scheduling outcome, aiding in analysis and debugging.
- **Robust Evaluation:** Includes multiple evaluation strategies to assess the fitness of chromosomes based on job completion times.

## Usage
- **Setup:** Define the number of machines and jobs, and initialize the genetic algorithm parameters.
- **Input:** Load job and machine data from user input or a CSV file.
- **Execution:** Run the genetic algorithm to generate optimized job scheduling.
- **Visualization:** View the scheduling results as a Gantt chart.



# AI-Driven Job Shop Scheduling System

## 🌟 Project Overview

Welcome to the GitHub repository for the AI-Driven Job Shop Scheduling System! This project was developed as part of the ENCS 3340 Artificial Intelligence course at the Faculty of Engineering and Technology. Utilizing a Genetic Algorithm, this system optimizes the scheduling of operations in a manufacturing plant, ensuring that each product is processed in the most efficient sequence possible to minimize overall production time.

## 🚀 Features

- **Custom Genetic Algorithm**: Tailored to optimize scheduling by finding good approximations of the solution within the given constraints.
- **Dynamic Input Handling**: Capable of processing varying numbers of machines and jobs, each with its own sequence of operations.
- **Visualization with Gantt Charts**: Provides a clear, visual representation of the machine schedules, aiding in the interpretation and analysis of the scheduling algorithm's efficiency.

## ⚙️ Technical Aspects

### Technologies Used
- **Python**: Core programming language for developing the scheduling algorithm and managing input/output operations.
- **Matplotlib**: Used for generating Gantt charts that visually represent the scheduling results.

### Genetic Algorithm Components
- **Chromosome Representation**: A chromosome encapsulates a feasible scheduling solution, represented by a dictionary mapping each machine to a sequence of operations.
- **Fitness Function**: Assesses the quality of schedules by calculating the sum of the finish times for all machines, where a lower sum indicates a better schedule.
- **Genetic Operators**: Includes crossover and mutation specifically designed to maintain valid job sequencing and machine assignments.

## 📊 AI and Analytical Skills

This project exemplifies the application of artificial intelligence in solving complex optimization problems. Here's how AI and analytical skills are pivotal:
- **Heuristic Search Techniques**: The genetic algorithm explores feasible solutions using methods inspired by natural selection.
- **Constraint-Based Optimization**: Manages multiple scheduling constraints, ensuring that each job's operational sequence is adhered to without interruption.
- **Algorithmic Efficiency**: Focuses on optimizing the algorithm's parameters like population size, crossover rate, and mutation rate to enhance performance.

## 📝 How to Use

1. **Clone the Repository**: Get the code by cloning this repository.
2. **Prepare Your Dataset**: Customize the `jobs.txt` to reflect your manufacturing schedule needs.
3. **Run the System**: Execute the `scheduler.py` to see the algorithm in action.
4. **View Results**: Analyze the output Gantt charts to assess the efficiency of your schedules.

## 📈 Example Output

Here's an example of a Gantt chart produced by our scheduling system, demonstrating its capability to efficiently allocate time and resources:

![Gantt Chart Example](images/gantt_example.png)

## 🧠 Lessons Learned


## Example
```python
from main import main
# Run the main function to start the scheduling system
main()



---

*For further exploration and more test cases, refer to the full project report.* [Link to full report](#)

