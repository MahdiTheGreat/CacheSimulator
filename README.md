# cacheSimulator
This project is based on Chapter 5 of Hennessy & Pattersons Computer Architecture: A Quantitative Approach.
The type of simulator we have built is known as a trace-driven simulator because it takes as input a trace of events, in this case, memory references. The trace was acquired on another machine. Once acquired, it can be used to drive simulation studies. In this project, the memory reference events specified in the trace(s) will be used by the simulator to drive the movement of data in and out of the cache, thus simulating its behavior. Trace-driven simulators are very effective for studying caches. This simulator supports the following configurations:

- Total cache size
- Block size
- Unified vs. split I- and D-caches (Von Neumann. vs. Harvard)
- Associativity
- Write back vs. write through
- Write allocate vs. write no-allocate

For more information on write policies and write-miss policies we can use the link below:
https://en.wikipedia.org/wiki/Cache_(computing)#Writing_policies

In addition to implementing the functionalities listed above, our simulator also collects and reports several statistics that will be used to verify the correctness of the simulator. In particular, our simulator tracks:

- Number of instruction references
- Number of data references
- Number of instruction misses
- Number of data misses
- Number of words fetched from memory
- Number of words copied back to memory

# Files

There are three trace files that we use to test the simulator. Their names are “spice.trace,” “cc.trace,” and “tex.trace.” These files are the result of tracing the memory reference behavior of the spice circuit simulator, a C compiler, and the TeX text formatting program, respectively. They represent roughly 1 million memory references each. For our testing purposes, we can slice any part of the files and use them as test cases, sincet testing the entirety of any one of these files could take a very long time and would probably use a significant portion of the computer’s resources.

The trace files are in ASCII format, so they are in human-readable form. Each line in the trace file represents a single memory reference and contains two numbers: a reference type, which is a number between 0–2, and a memory address. All other text following these two numbers are ignored by our simulator. The reference number specifies what type of memory reference is being performed with the following encoding:

0 Data load reference
1 Data store reference
2 Instruction load reference

The number following the reference type is the byte address of the memory reference itself. This number is in hexadecimal format, and specifies a 32-bit byte address in the range 0-0xffffffff, inclusive.

# Building the Cache Model

We build the simulator by incrementally adding functionality, by following the incremental approach below:
1. Build a unified, fixed block size, direct-mapped cache with a write-back write policy and a write-allocate allocation policy.
2. Add variable block size functionality.
3. Add variable associativity functionality.
4. Add split organization functionality.
5. Add write-through write policy functionality.
6. Add write no-allocate allocation policy functionality.

Once we have built a direct-mapped cache, we extend it to handle set-associative caches by allowing multiple cache lines to reside in each set. In the case of a direct-mapped cache, the eviction is easy since there is at most one cache line in every set. In this assignment, we will implement an LRU replacement policy. 

Once we have built a direct-mapped cache, we can extend it to handle set-associative caches by allowing multiple cache lines to reside in each set. We implement this by using doubly linked-lists in the place of the set. Our simulator,however, does not allow the number of cache lines in each linked list to exceed the degree of associativity configured in the cache.
If we ever need to insert a cache line into a set that is already at full capacity, then it is necessary to evict one of the cache lines. In the case of a direct-mapped cache, the eviction is easy since there is at most one cache line in every set. When a cache has higher associativity, it becomes necessary to choose a cache line for replacement. In this project, we will implement an LRU replacement policy by keeping the linked list in each set sorted by the order in which the cache lines were referenced. This is be done by removing a cache line from the linked list each time we reference it, and inserting it back into the linked list at the head. In this case, we always evict the cache line at the tail of the list.

We should keep in mind that by implementing a set associative cache whose associativity can be configured, then we have also implemented a fully associative cache. A fully associative cache is simply an N-way set-associative cache with 1 set, and in which N is the total number of cache lines in the cache.

# Input Format

Our program reads inputs in the following form. Note that entries marked with <>s will be replaced with user-defined inputs while the dashes are constant and will be entered to separate the inputs from each other.
First, our program reads a line as shown below:

<block size> - <unified or separated> - <associativity> - <write policy> - <write_miss policy>

Explanation for each of the entries:
- <block size>: Cache’s block size in bytes which should be a power of 2. (e.g. 8, 64, 1024...)
- <unified or separated>: An indicator of cache’s architecture. “0” Denotes Von Neumann and “1” denotes Harvard.
- <associativity>: An integer indicating how associative the cache is. Remember that the cache’s size (explained shortly) should be divisible by its associativity.
- <write policy>: A string that should be either “wb” (write-back) or “wt” (write-through).
- <write_miss policy>: A string that should be either “wa” (write-allocate) or “nw” (no-write allocate)

Then, if <unified or separated> is 0, your program should read a line as follows:

<unified size>

Which is the cache’s size in bytes while being a power of 2. Otherwise, if <unified or separated> is 1, your program should read the following line:

<instruction cache size> - <data cache size>

Both of which are the respective caches’ sizes in bytes while being powers of 2. Then, our program assumes the cache is empty and start reading trace entries as specified before. Some examples are provided alongside this file for the matter to be even clearer. In some of the examples, there exists a third column which is only a human-readable guidance to explicitly explain the cache’s response to the requests and is of no other value.

# Output Format

Our program prints its result of the cache’s statistics using standard output (e.g. printf in C, System.out.Print in Java, etc.). Note that we assume a 32-bit architecture, therefore a block is made out of 4 bytes - as used in the TRAFFIC part of the output samples that are provided alongside this file-. Also remember that the “demand fetch” and “copies back” parts of the samples refer to the number of words fetched from memory and the number of words copied back to memory respectively.

# Testing
For testing, we use the test.zip and for results of tests for crosschecking, we use result.zip.
