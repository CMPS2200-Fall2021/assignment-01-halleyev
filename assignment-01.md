

# CMPS 2200 Assignment 1

**Name:**________Halley Vance_________________


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. **Asymptotic notation**

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  
.  Yes, because a constant k > 2 times 2^n is an upper bound for 2^n+1
.  
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  
.  
.  No, because when you take the log2 of both functions nlog2 is not an upper bound for 2^n(log2)
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  
.  No, because log^2n is not an upper bound for n^1.01
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  
.  Yes, because log^2n is a lower bound for n^1.01
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  
.  Yes, because (logn)^3 times a constant k is an upper bound for sqrt(n)
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  
.  No, because (logn)^3 times a constant k is not a lower bound for sqrt(n)
.  
.  

  - 1g. Consider the definition of "Little o" notation:
  
$g(n) \in o(f(n))$ means that for **every** positive constant $c$, there exists a constant $n_0$ such that $g(n) \le c \cdot f(n)$ for all $n \ge n_0$. There is an analogous definition for "little omega" $\omega(f(n))$. The distinction between $o(f(n))$ and $O(f(n))$ is that the former requires the condition to be met for **every** $c$, not just for some $c$. For example, $10x \in o(x^2)$, but $10x^2 \notin o(x^2)$.  

.  

**Prove** that $o(g(n)) \cap \omega(g(n))$ is the empty set.  

.  
.  Since one is always an upper bound and one is always a lower bound and they never are equal, they never intersect. Therefore is an empty set. 
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  



2. **SPARC to Python**

Consider the following SPARC code:  
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. What does this function do, in your own words?  

.  
.  
.  
.  
.  
.  
  


3. **Parallelism and recursion**

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. What is the Work and Span of this implementation?  

.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3c. Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. What is the Work and Span of this sequential algorithm?  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3e. Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  
.  
.  
.  
.  
.  
.  
.  

