from Process import *
import re
import random
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.ticker as ticker
import copy
import gc

import csv

import tkinter as tk
from tkinter import filedialog

# Initialize Global variable
machines_number: int = 0
jobs_number: int = 0
processes_number: int = 0
jobs_process_lists: list = []
total_duration = 0

# Initialize Parameters
population_size: int = 18
population_list: list = []

crossover_rate = 0.8
mutation_rate = 0.3
n_generations = 200


# Function to parse the input string and create a list of Process instances
def create_processes_from_string(input_string):
    """
    :rtype: list
    """
    global total_duration
    processes = []

    # Extract the job number
    job_match = re.match(r"J(\d+):", input_string)
    if job_match:
        job_number = int(job_match.group(1))
    else:
        raise ValueError("Invalid input: Job number not found")

    # Extract the machine and duration information
    machine_pattern = r"M(\d+)\((\d+)\)"  # Matches patterns like M1(10)
    machine_matches = re.findall(machine_pattern, input_string)

    for sequence_number, (machine_number, duration) in enumerate(machine_matches):
        machine_number = int(machine_number)
        duration = int(duration)
        process = Process(job_number, machine_number, sequence_number, duration)
        total_duration += duration
        processes.append(process)

    total_duration *= jobs_number
    return processes


def input_test2():
    # Refer to these global variable
    global processes_number
    global jobs_process_lists
    global machines_number
    global jobs_number

    print('Welcome to Program')

    machines_number = int(input('Please Enter number of machines : '))
    jobs_number = int(input('Please Enter number of jobs : '))

    # Create array of lists based on jobs:
    jobs_process_lists = [[] for _ in range(jobs_number)]

    # Sample input : "J1: M1(10), M2(5), M3(15)"
    jobs_process_lists[0] = create_processes_from_string('J0: M0(5), M2(4), M0(15)')
    processes_number += len(jobs_process_lists[0])

    # second
    jobs_process_lists[1] = create_processes_from_string('J1: M1(10), M3(2), M2(15), M1(3)')
    processes_number += len(jobs_process_lists[1])

    # third
    jobs_process_lists[2] = create_processes_from_string('J2: M2(10), M1(5), M3(15)')
    processes_number += len(jobs_process_lists[2])

    print('Number of proccesses is ' + str(processes_number))


def choose_file():
    # Create a root window (it will not be shown)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Show the file chooser dialog
    file_path = filedialog.askopenfilename(
        title="Select a file",
        #filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    # Print the chosen file path
    if file_path:
        print("Selected file:", file_path)
    else:
        print("No file selected")

    return file_path


def input_file(file):
    # Refer to these global variable
    global processes_number
    global jobs_process_lists
    global machines_number
    global jobs_number
    global total_duration

    print('Welcome to Program')

    machines_number = int(input('Please Enter number of machines : '))
    jobs_number = int(input('Please Enter number of jobs : '))

    count = 0

    # Create array of lists based on jobs:
    jobs_process_lists = [None for _ in range(jobs_number)]

    # Read input from CSV file
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)

        # each row is a job
        for row in reader:
            print(row)
            jobs_process_lists[count] = []
            sequence_number = 0
            data = row[0].split(',')

            # Extract job number
            job_number = data[0][1:]  # Remove the 'J' prefix

            # Extract machine numbers and durations
            for operation in row[1:]:
                if len(operation) > 0:
                    operation = operation.strip()  # Remove leading/trailing whitespaces
                    print(operation)

                    machine_number, duration = operation.split('-')
                    machine_number = machine_number[1:]
                    processes_number += 1

                    process = Process(int(job_number), int(machine_number), int(sequence_number), int(duration))
                    jobs_process_lists[count].append(process)
                    sequence_number += 1
                    total_duration += int(duration)

            count += 1

    total_duration *= machines_number
    print("total time is " + str(total_duration))
    print("--------")
    print(jobs_process_lists)


def generate_initial_population():
    global jobs_process_lists
    global jobs_number

    while len(population_list) < population_size:

        chromosome = Chromosome(machines_number, jobs_number)

        current_indices = [0 for _ in range(jobs_number)]

        # current chromosome length
        length = 0
        i = 0

        while length < processes_number:

            list_number = i % jobs_number

            random_int = random.randint(0, len(jobs_process_lists[list_number]) - current_indices[list_number])
            #print('random is ' + str(random_int) + ' list number ' + str(list_number))

            length += random_int  # this is wrong

            #print('testing this = ' + str(current_indices[list_number]) + "----" + str(
            #current_indices[list_number] + random_int))

            for j in range(current_indices[list_number], current_indices[list_number] + random_int):
                print(jobs_process_lists[list_number][j])
                chromosome.add_process(jobs_process_lists[list_number][j])
                #test.append(jobs_process_lists[list_number][j])

            current_indices[list_number] += random_int

            # print("-----")
            # for index in current_indices:
            #     print(index)
            #
            # print("-----")

            i += 1

        #print(chromosome)
        population_list.append(chromosome)

    #for process in test:
    #print(process)


def evaluate_chromosome(chromosome: Chromosome):
    """     version 2 on finish time of the machines
    :param chromosome:
    :return:int
    """
    global total_duration

    # print("hi from evaluate ")

    print('ok 6')
    finish_times =chromosome.create_schedule()

    if chromosome.evaluation == -1:
        return -1

    machines_lists = chromosome.processes

    evaluation: int = 0

    for machine_number, process_list in machines_lists.items():
        time= process_list[-1].start + process_list[-1].duration
        #time+=max(finish_times)
        #time = process_list[-1].start
        # print(time)
        evaluation += time

    print('ok 6')
    print(evaluation)
    # print(total_duration - evaluation)

    chromosome.evaluation = total_duration - evaluation
    return total_duration - evaluation


def evaluate_chromosome2(chromosome: Chromosome):
    """     version 2 on finish time of the max
    :param chromosome:
    :return:int
    """
    global total_duration

    # print("hi from evaluate ")

    print('ok 6')
    finish_times = chromosome.create_schedule()

    if chromosome.evaluation == -1:
        return -1

    evaluation: int = 0

    max_value = max(finish_times)
    print(max_value)

    # for time in finish_times:
    #     # print(time)
    #     evaluation += time

    print('ok 6')
    # print(evaluation)
    # print(total_duration - evaluation)

    chromosome.evaluation = total_duration - max_value
    return total_duration - max_value


def evaluate_chromosome2(chromosome: Chromosome):
    """
    evaluate on finish of jobs
    :param chromosome:
    :return:int
    """
    global total_duration

    #print("hi from evaluate ")

    print('ok 6')
    finish_times = chromosome.create_schedule()
    #machine_lists = chromosome.processes
    #finish_times = [0 for _ in range(jobs_number)]

    # for machine_number, process_list in chromosome.processes.items():
    #     for process in process_list:
    #         current_job = process.job_number
    #         current_finish = process.start + process.duration
    #         finish_time = max(current_finish, finish_times[current_job])
    #         finish_times[current_job] = finish_time

    if chromosome.evaluation == -1:
        return -1

    evaluation: int = 0

    #print("Finish Times:")
    for time in finish_times:
        #print(time)
        evaluation += time

    print('ok 6')
    #print(evaluation)
    #print(total_duration - evaluation)

    chromosome.evaluation = total_duration - evaluation
    return total_duration - evaluation


def draw_gannt_chart(chromosome: Chromosome):
    chromosome.create_schedule()

    machine_lists = chromosome.processes
    #print(machine_lists)
    #print(str(len(machine_lists)))

    # Initialize a list of named colors and shuffle for randomness
    colors = list(mcolors.CSS4_COLORS.keys())
    random.shuffle(colors)

    # Assign a unique color to each job number
    #job_numbers = {process.job_number for machine in machine_lists for process in machine}
    #job_color_map = {job: colors[i % len(colors)] for i, job in enumerate(sorted(job_numbers))}

    job_numbers = range(jobs_number)

    # Assign a unique color to each job number
    # The job numbers are already in order, so we can directly assign colors
    job_color_map = {job: colors[job % len(colors)] for job in job_numbers}

    # Create a new figure and axis
    fig, ax = plt.subplots()

    # Loop through the machines and their associated processes
    for machine_number, process_list in machine_lists.items():

        if len(process_list) == 0:
            ax.barh(y=machine_name, left=0, width=0, height=0.4, color="lightgray", alpha=0.5,
                    edgecolor="black")  # Placeholder bar
        else:
            for process in process_list:
                job_number = process.job_number  # Get the job number for color mapping
                start_time = process.start  # Start time of the process
                duration = process.duration  # Duration of the process

                # Add a horizontal bar for each process, with color based on job number
                machine_name = ("M" + str(machine_number))
                ax.barh(
                    y=machine_name,  # Machine name for the y-axis
                    left=start_time,  # Start time for the left position
                    width=duration,  # Duration for the width of the bar
                    height=0.4,  # Bar thickness
                    color=job_color_map[job_number],  # Color based on job number
                    label=f"Job {job_number}" if f"Job {job_number}" not in ax.get_legend_handles_labels()[1] else None,
                    # Unique legend label
                )

    # Customize the time axis with more divisions
    ax.xaxis.set_major_locator(ticker.MultipleLocator(5))  # Major ticks every 5 units
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))  # Minor ticks every 1 unit

    # Customize the format of the ticks
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x:.1f}"))  # Format as float with 1 decimal place

    # Set axis labels and title
    ax.set_xlabel("Time")  # Label for the x-axis
    ax.set_ylabel("Machine")  # Label for the y-axis
    ax.set_title("Job Scheduling")  # Chart title

    # Display legend to identify jobs (if labels are unique)
    ax.legend()

    #plt.title("Chromosome Representation")

    fig.canvas.manager.set_window_title("Chromosome Representation")

    # Show the Gantt chart
    plt.show()  # Display the chart


def evaluate_population(population_list):
    total_fitness = 0

    # evaluate current population
    for chromosome in population_list:
        print("infinite loop")
        evaluate_chromosome(chromosome)
        print("done evaluation")
        total_fitness += chromosome.evaluation

        # Create a roulette wheel
    wheel = []
    for chromosome in population_list:
        if chromosome.evaluation == -1:
            probability = 0
        else:
            probability = chromosome.evaluation / total_fitness
        print("p " + str(probability))
        wheel.extend([chromosome] * int(probability * 100))  # Scale probabilities to integers for selection

    #print(wheel)
    return wheel


def select_chromosome(wheel):
    # Select individuals (parents) based on the roulette wheel
    chosen = random.choices(wheel, k=1)[0]
    return chosen


# def select_random(wheel):
#     # Select individuals (parents) based on the roulette wheel
#     chosen = random.choices(wheel, k=1)[0]
#
#     return chosen

def cross_over(parent1: Chromosome, parent2: Chromosome):
    #population_list.remove(parent1)
    #population_list.remove(parent2)

    offspring1 = copy.deepcopy(parent1)
    offspring2 = copy.deepcopy(parent2)

    random_int = random.randint(0, machines_number - 1)
    #random_int = 1

    print("at : " + str(random_int))

    # suppose single cross point (the two jobs lists on different machines)
    machines1 = parent1.processes
    machines2 = parent2.processes

    print("ok1")
    temp1 = machines1[random_int]
    temp2 = machines2[random_int]

    print("ok2")
    offspring1.processes[random_int] = temp2
    offspring2.processes[random_int] = temp1

    print("ok3")
    #evaluate_chromosome(offspring1)
    offspring1.create_schedule()
    if offspring1.evaluation == -1:
        print("******this offspring1 wrong********")

    #evaluate_chromosome(offspring2)
    offspring2.create_schedule()

    if offspring2.evaluation == -1:
        print("******this offspring2 wrong********")

    #offspring1.create_schedule()
    #offspring2.create_schedule()

    print("ok4")

    print("done crossover")

    return offspring1, offspring2
    #return chromosomes_to_compare[0], chromosomes_to_compare[1]


def mutation(chromosome):
    print("muation")

    random_machine = random.randint(0, machines_number - 1)
    machine_list = chromosome.processes[random_machine]

    print(machine_list)

    if len(machine_list) <= 2:
        return

    random_index = random.randint(1, len(machine_list) - 2)
    print(random_index)
    print(machine_list[random_index])
    print(machine_list[random_index + 1])

    if machine_list[random_index].job_number != machine_list[random_index + 1].job_number:
        machine_list[random_index], machine_list[random_index + 1] = machine_list[random_index + 1], machine_list[
            random_index]
        print("swapped")
    else:
        print("no mutation")
        return False

    chromosome.create_schedule()

    if chromosome.evaluation == -1:
        print("******this is wrong********")
        return False

    print('done mutation')
    return True

    #return offspring


def create_next_generation(population_list):  # see this
    global crossover_rate
    global mutation_rate

    wheel = evaluate_population(population_list)

    offspring_list = []

    # take amount of valid chromomses
    while len(offspring_list) < (crossover_rate * population_size):
        parent1 = select_chromosome(wheel)
        parent2 = select_chromosome(wheel)

        offspring_1, offspring_2 = cross_over(parent1,
                                              parent2)

        evaluate_chromosome(offspring_1)
        evaluate_chromosome(offspring_2)

        if offspring_1.evaluation != -1:
            offspring_list.append(offspring_1)

        if offspring_2.evaluation != -1:
            offspring_list.append(offspring_2)

    # the reaming are the best of the currrnt population
    remaining = population_size - len(offspring_list)

    sorted_chromosomes = sorted(population_list, key=lambda x: x.evaluation, reverse=True)
    top_chromosomes = sorted_chromosomes[:remaining]

    new_generation = offspring_list + top_chromosomes

    # apply random mutation on new population
    num_mutation = mutation_rate * population_size
    random.shuffle(new_generation)

    count = 0
    while count < num_mutation:
        random_integer = random.randint(0, len(population_list) - 1)
        if mutation(population_list[random_integer]) == True:
            count += 1

    return new_generation


def run():
    global population_list
    print("Welcome to our scheduling System ")

    input_file('inputSample_4x3.csv')
    generate_initial_population()

    print("done random")

    print("done here")
    print("Initial Generation G0")

    # Loop through the list and evaluate each chromosome
    #for i, chromosome in enumerate(population_list):
        #print(f"{i}: evaluation is = {chromosome.evaluation}")

    count = 0
    max_evaluation = 0
    n=0
    while count<30 :
        n+=1

        population_list = create_next_generation(population_list)

        max_chromosome = max(population_list, key=lambda x: x.evaluation)
        prev_max = max_evaluation
        max_evaluation = max_chromosome.evaluation

        if max_evaluation == prev_max:
            count += 1
        else:
            count=0

        for i, chromosome in enumerate(population_list):
            print(f"{i}: evaluation is = {chromosome.evaluation}")

    print("stopped at " +str(n))
    print("The max chromosome found with evaluation" + str(max_chromosome.evaluation))

    while True:
        num = int(input('what chromosome would you like to see?'))

        chromosome = population_list[num]
        draw_gannt_chart(chromosome)


run()
