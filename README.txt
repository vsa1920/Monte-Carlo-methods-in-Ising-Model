The code has been partitioned into parts :-

Here is a general outline of the functioning of various parts.
1) Animation:-
A self sufficient code. Generates an animation of the simulation of the Metropolis Algorithm in Ising (metropolis.py) and Planar (planar.py) models.
To change the temperature change variable T at the start of the metropolis.py. planar.py has only animation for quenching the system.

2) Each of Metropolis, Wolff, Planar and Spin Glass is divided into:-
i) Equilibrium:-
Generates states at equilibrium for various temperatures and stores them as text files. These text files are then supposed to be copied to the Measurement
folder before running the measurement program. To get states at various temperatures, update the list (T_lst) in the Equilibrium.py program

ii) Measurement:-
Measures all the quantities. To run measurement first paste all the equilibrium state text files inside this folder and update the T_lst. Run the program to 
obtain Output.txt. 

iii) Generate Plots:-
Paste the obtained Output.py to obtain specific heat and/or magnetisation-susceptibility plots.
a) Plot.py :- Run this code to obtain plots.
b) Analytical.py :- Needed by Plot.py to plot the analytical solutions to the Ising Model.

3) Other important code fragments include:-
i) Metropolis.py / Wolff.py / Parallel Tempering:-
The main body of the functions that simulate the systems. 

ii) Analyze.py
Has important functions needed during simulations such as evaltuation of energy and specific heat or function to read a given state.

4) State plots
To get an imshow image of any state, copy and paste the state text file to State plots and run State_plots.py.

THE RUNTIME FOR EACH STEP MIGHT BE FROM 2-3 HOURS. TO SAMPLE A SMALLER SIMULATION, REDUCE THE TIME VARIABLES AT THE START OF THE CODE AND RUN FOR ONE OR
TWO TEMPERATURES IN THE T_lst AT A TIME. THE RUNTIME OF PARALLE TEMPERING IS A FEW MINUTES.


