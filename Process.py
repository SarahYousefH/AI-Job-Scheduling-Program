# Define the Process class
from typing import List, Any


class Process:

    def __init__(self, job_number, machine_number, sequence_number, duration):
        # Initialize the attributes
        self.job_number = job_number
        self.machine_number = machine_number
        self.sequence_number = sequence_number
        self.duration = duration
        self.start = 0

        # todo : add more attributes as needed

    def __repr__(self):
        # String representation of the class instance for debugging
        return (f"Process(job_number={self.job_number}, machine_number={self.machine_number}, "
                f"sequence_number={self.sequence_number}, duration={self.duration}), start={self.start})")

    def __str__(self):
        # Provide a user-friendly string representation
        return (f"Job {self.job_number} on Machine {self.machine_number} - "
                f"Sequence {self.sequence_number} with Duration {self.duration}"
                f"starts at {self.start}")

    def __eq__(self, other):
        if isinstance(other, Process):
            return self.job_number == other.job_number and self.sequence_number == other.sequence_number and self.machine_number == other.machine_number
        return False


# Example of creating an instance of Process
p = Process(job_number=1, machine_number=2, sequence_number=3, duration=120)


# Print the instance
# print(p)
#
# # Check the attributes
# print("Job number:", p.job_number)
# print("Machine number:", p.machine_number)
# print("Sequence number:", p.sequence_number)
# print("Duration:", p.duration)


# Chromosome class
class Chromosome:

    def __init__(self, machines_number, jobs_number):
        self.machines_number = machines_number
        self.jobs_number = jobs_number
        # List of processes
        self.processes: Dict[int, List[Process]] = {i: [] for i in range(machines_number)}
        #self.processes: List[List[Process]] = [[] for _ in range(n)]
        self.evaluation: int = 0
        # todo : add more attributs as needed

    def add_process(self, process):
        # Add a process to the list
        self.processes[process.machine_number].append(process)

    def __repr__(self):

        # String representation for debugging
        return f"Chromosome(processes={self.processes})"

    def __str__(self):
        # User-friendly string representation
        process_str = ', '.join([str(p) + "\n" for p in self.processes])
        return f"Chromosome with processes:\n {process_str}"

    def __gt__(self, other):
        # Greater than comparison based on evaluation
        if not isinstance(other, Chromosome):
            return NotImplemented
        return self.evaluation > other.evaluation

    def __lt__(self, other):
        # Less than comparison based on evaluation
        if not isinstance(other, Chromosome):
            return NotImplemented
        return self.evaluation < other.evaluation



    def print_processes(self):
        for machine_number, process_list in self.processes.items():
            print(f"Machine Number {machine_number}:")
            for process in process_list:
                print(process)

        print("------------------------------------------")

    def create_schedule(self):
        print('creating schedule')

        #self.print_processes()

        #intialize all strats to zero
        for machine_number, process_list in self.processes.items():
            for process in process_list:
                process.start = 0

        count = 0

        # Create arrays to help in scheduling :
        jobs_times = [0 for _ in range(self.jobs_number)]
        jobs_sequence = [0 for _ in range(self.jobs_number)]
        machine_indexes = [0 for _ in range(self.machines_number)]

        length = 0
        prev_length = 0
        current_machine = 0

        processes_number = 9

        while length < processes_number:

            # if count==processes_number and length==0:
            #     self.evaluation=-1
            #     break

            if length == prev_length:
                count += 1

            if count == processes_number:
                self.evaluation = -1
                break

            #print("hi3")
            current_machine = current_machine % self.machines_number

            current_index = machine_indexes[current_machine]
            #print("indexxx" + str(current_index))
            process_list = self.processes[current_machine][current_index:]

            if len(process_list) == 0:
                current_machine += 1
                continue

            #print("current machine " + str(current_machine))
            #print("current index" + str(current_index))

            for process in process_list:
                #print("hi2")
                if process.sequence_number == jobs_sequence[process.job_number]:

                    current_index = machine_indexes[process.machine_number]

                    # update
                    jobs_sequence[process.job_number] += 1
                    machine_indexes[process.machine_number] += 1

                    start_time = 0

                    # if first in the machine
                    if process == self.processes[process.machine_number][0]:
                        #print("true")
                        start_time = jobs_times[process.job_number]
                    else:
                        #print("yes")
                        #print(str(self.processes[process.machine_number][current_index - 1].start +
                        #self.processes[process.machine_number][current_index - 1].duration))

                        start_time = max(jobs_times[process.job_number], (
                                self.processes[process.machine_number][current_index - 1].start +
                                self.processes[process.machine_number][current_index - 1].duration))

                    process.start = start_time
                    jobs_times[process.job_number] = (process.start + process.duration)

                    #print("ss" + str(start_time))

                    length += 1
                    count = 0
                    #print ("length is " +str(length))

                    # if process == self.processes[process.machine_number][-1]:
                    #     current_machine += 1
                    #     break

                else:
                    #print("hiiiiiiiiii")
                    # go to next machine
                    current_machine += 1
                    break

                prev_length = length

        return jobs_times
