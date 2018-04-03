# Mini Project 1

## Students

1.  Saleem Hadad ```1337379```
2.  Ahid Naif Alqaud  ```1410721```

## Solution

*   **Question 1**:  Using MATLAB/SciLab/Octave

    *   a. Plot the sampled signal *x*(*n*). Label the axes properly. Show your work 

    ```matlab
    % sampling frequency
    fs = 60; 

    % sampling period
    t = 1/fs; 

    % end point on n-axis
    ns = 3; 

    % range of n axis -- it's divided by fs to get the sampled signal
    n = 0:1/fs:(ns-1/fs); 

    %sampled function
    f = cos(2*pi*10*n) + 2*cos(2*pi*20*n) - cos(2*pi*36*n) + cos(2*pi*50*n); 
    N = size(f,1);

     % plot sampled signal
    figure;
    stem(n, f);
    xlabel ('n'); ylabel('f[n]');

    figure;
    f = fftshift(fft(f));

    % plot amplitude specturm
    stem (abs(f)/N); 
    xlabel ('f [Hz]'); ylabel ('|X(f)|');
    ```

    >   Plot

    ![q1-1](/Users/saleem/Desktop/q1-1.png)

    ​

    *   b. Plot the **amplitude spectrum **of *x*(*n*). Label the axes properly. Show your work (**hint**: use the command fftshift). 

    >   Plot

    ![q1-2](/Users/saleem/Desktop/q1-2.png)

    *   c. What is your conclusion? 

    We conclude that some of the frequencies could cause aliasing due to the fact they are grater than fs/2.

    ​

*   **Question 2**: *Discrete-time system*. Consider the following discrete-time system:

     𝑦(𝑛)=1.2𝑦(𝑛−1)−0.31𝑦(𝑛−2)+10𝑥(𝑛−1)+6𝑥(𝑛−2)

    *   a. Compute manually the zero-state response to the unit step input, 𝑥(𝑛)=𝑢(𝑛). 

        $y(z) = 1.2z^-1 - 0.31z^-2Y(z) + 10z^-1X(z) + 6z^-2X(z)$

        $Y(z)[1 - 1.2z^-1+031z^-2] = X(z)[10z^-1+6z^-2]$

        $Y(z)=(\frac{10z^-1+6z^-2}{1 - 1.2z^-1+031z^-2}) X(z)$

        $Y(z)=\frac{(10z+6) z}{(z^2-1.2z+0.31)} * (z-1)$

        => $\frac{Y(z)}{z} = \frac{z*(10z+6)} {z*(z-0.824)*(z-0.376)*(z-1)}$

          	    $ = \frac{A}{Z} + \frac{B}{z-0.824} + \frac{C}{z-0.376} + \frac{D}{z-1}$

        let $z=0.824​$ => $B=-181​$

        let $z=0.376$ => $C=35$

        let $z=0.1$ => $D=145.5$

        let $z=0$ => $A=0$

        >   **$y(n)=[-181(0.824)^n+35(0.376)^n+145.5] * u(n)$**

        ​

    *   $b$. Plot the step response using MATLAB/SciLab/Octave. Hint: set the ranges 0≤𝑛≤50 and 0≤𝑦(𝑛)≤140. 

    ```matlab
    % initialize range of n-axis
    n = (0:50);

    %initialize step input function
    x = inline('(1.^(n)).*(n>=0)','n'); 

    % coefficients of y(n)/ left side of the difference equation
    a = [1 -1.2 0.31]; 

    % coefficients of x(n)/ right side of the difference equation
    b = [0 10 6]; 

    % find the zero state response
    y = filter (b,a,x(n)); 

    % f is the function we have got manually
    f = inline('(145.5 - 181*(0.824.^(n)) + 35*(0.376.^(n))).*(n>=0)','n'); 

    subplot(2,1,1);

    % plot the zero state response we got by using matlab 
    stem(n,y); 
    ylabel('y[n] using matlab');

    subplot(2,1,2);

    % plot zero state response we got manually to compare them together
    stem(n, f(n)); 
    xlabel ('n'); ylabel('f[n] - manually');
    ```

    ​

    >   Plot

    ![q2-1](/Users/saleem/Desktop/q2-1.png)

    ![q2-2](/Users/saleem/Desktop/q2-2.png)