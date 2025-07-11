from pathlib import Path

n_tasks = [
    40,
    50,
    100,
]

n_lines = [2, 3, 5]


PATH = Path(__file__).parent.parent
for n_task, n_line in zip(n_tasks, n_lines):

    with open(PATH / f"original/wt{n_task}.txt", "r") as f:
        lines = f.readlines()
        matrix = [[value for value in line.strip().split(' ') if value.isdigit()] for line in lines]
    
    with open(PATH / f"original/wt{n_task}opt.txt", "r") as f:
        lines = f.readlines()
        opt_values = [x.strip().split(', ') for x in lines]
    
    ptr = 0
    for instance_id in range(125):
        processing_times = sum(matrix[ptr:ptr+n_line]           , [])
        weights          = sum(matrix[ptr+n_line:ptr+2*n_line]  , [])
        due_dates        = sum(matrix[ptr+2*n_line:ptr+3*n_line], [])

        with open(PATH / f"wt{n_task}_{instance_id+1}.txt", "w") as f:
            f.write(f"{n_task}\n")

            for task in range(n_task):
                f.write(f"{processing_times[task]} {weights[task]} {due_dates[task]}\n")
        
            f.write("---\n")

            ub, optimal = map(int, opt_values[instance_id])

            f.write(f"Objective UB: {ub}\n")
            f.write(f"Objective Optimal: {optimal}\n")

        ptr += 3*n_line
