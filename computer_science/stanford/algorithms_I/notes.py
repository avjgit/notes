I. INTRODUCTION
Introduction : Why Study Algorithms ? (19 min)     
About the Course (17 min)     
Merge Sort: Motivation and Example (9 min)     
    better than Selection, Insertion, Bubble
Merge Sort: Pseudocode (13 min)
    ok. linear time. ln(n) time
Merge Sort: Analysis (9 min)     
Guiding Principles for Analysis of Algorithms (15 min)     
    worst case
    averge case
    benchmarks
    
    won't pay attention to constant, lower-order terms (like 4 in 4h+2)
        1) easier
        2) constants depend on language and compiler, and architecture
        3) lose very little prediction power
    
    asymptotic analysis: focus on running time for very large inputs
    
    "fast" means - worst case growing slowly with input size
    
    
II. ASYMPTOTIC ANALYSIS
Big-Oh Notation (4 min)     
    so, big O means, it is possible to multiply f(n) with some constant C,
        and receive result > T(n)
Basic Examples (7 min)     
    f(n**k), there exists such n, so that f is always > C* n**(k-1)
Big Omega and Theta (7 min)     
    T(n) = Omega(f(n)), if exists such C so C*f(n) < Tn)
    Theta - is O and Omega
    small o is when function is growing strictly less than other
    Knuth 1976
Additional Examples [Review - Optional] (8 min)     

III. DIVIDE & CONQUER ALGORITHMS
O(n log n) Algorithm for Counting Inversions I (13 min)     
O(n log n) Algorithm for Counting Inversions II (17 min)     
Strassen''s Subcubic Matrix Multiplication Algorithm (22 min)     
O(n log n) Algorithm for Closest Pair I [Advanced - Optional] (32 min)     
O(n log n) Algorithm for Closest Pair II [Advanced - Optional] (19 min)     

IV. THE MASTER METHOD
Motivation (8 min)     
Formal Statement (10 min)     
Examples (13 min)     
Proof I (10 min)     
Interpretation of the 3 Cases (11 min)     
Proof II (16 min)     

V. QUICKSORT - ALGORITHM
Quicksort: Overview (12 min)     
Partitioning Around a Pivot (25 min)     
Correctness of Quicksort [Review - Optional] (11 min)     
Choosing a Good Pivot (22min)     

VI. QUICKSORT - ANALYSIS
Analysis I: A Decomposition Principle [Advanced - Optional] (22 min)     
Analysis II: The Key Insight [Advanced - Optional] (12min)     
Analysis III: Final Calculations [Advanced - Optional] (9min)      

VII. PROBABILITY REVIEW
Part I [Review - Optional] (25 min)