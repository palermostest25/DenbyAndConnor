import subprocess

def get_kernels():
    global kernel_versions
    global current_kernel
    global kernels
    kernels=subprocess.run("dpkg --list | grep ^ii | grep linux-image-[0-9] | awk '{print $2}'", capture_output=True, text=True, shell=True)
    current_kernel=subprocess.run("uname -r", capture_output=True, text=True, shell=True)
    if isinstance(kernels, subprocess.CompletedProcess) and isinstance(current_kernel, subprocess.CompletedProcess):
        print("Kernel Get Sucsessful!")
        current_kernel = current_kernel.stdout.strip()
        kernels = kernels.stdout
        kernels = kernels.split('\n')
        kernels.pop()
    else:
        print("Kernel Get Error")
        exit()

    kernel_versions = []
    for kernel in kernels:
        kernel_versions.append(kernel.split('linux-image-')[1])

while True:
    choice = None
    get_kernels()
    kernel_print_loop = 1
    for version in kernel_versions:
        if version == current_kernel:
            print(f"{kernel_print_loop}. {version} ACTIVE")
        else:
            print(f"{kernel_print_loop}. {version}")
        kernel_print_loop += 1
    while True:
        try:
            kernel_to_remove = int(input("Kernel to remove: "))
            if not kernel_to_remove <= len(kernel_versions) or not kernel_to_remove > 0:
                int("hi")
            break
        except ValueError:
            print("Please choose one of the options")
            input("Press enter to continue")
    
    while True:
        try:
            if kernel_versions[kernel_to_remove - 1] == current_kernel:
                print("Error: cant remove active kernel!")
                break
            choice = input(f"Remove Kernel: {kernels[kernel_to_remove - 1]} [Y,N] ")
            choice = choice.capitalize()
            if not choice == 'Y' and not choice == "N":
                int("hi")
            break
        except ValueError:
            print("Please choose one of the options")
            input("Press enter to continue")
    if choice == "Y":
        subprocess.run(f"sudo apt remove {kernels[kernel_to_remove - 1]}", check=True, shell=True)
        subprocess.run(f"sudo update-grub", check=True, shell=True)



