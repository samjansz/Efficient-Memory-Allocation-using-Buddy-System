<h1>Efficient Memory Allocation using the Buddy System</h1>
<h3>Overview</h3>
<p>This project implements the Buddy System, a memory management algorithm designed to allocate and deallocate memory dynamically with minimal fragmentation. It uses Python to simulate memory allocation and deallocation, providing an interactive Command-Line Interface (CLI) for users to manage memory efficiently.</br>
Topics: #efficiency #memory-management #buddy-system #data-structures #computational-algorithms</p>

<h3>Features</h3>
<ul>
<li>Dynamic Memory Allocation: Allocates memory blocks of requested sizes.</li>
<li>Efficient Deallocation: Frees memory blocks and merges buddies to form larger blocks.</li>
<li>Tree-Based Representation: Memory is organized as a binary tree for efficient splitting and merging.</li>
<li>Interactive CLI: Users can allocate, deallocate, and view memory using simple commands.</li>
</ul>

<h3>Usage</h3>
<ol>
<li>Allocate Memory:</br>
```
python app.py --allocate <size_in_kb>
```
</li>
<li>Deallocate Memory:</br>
```
python app.py --deallocate <start_address>
```
</li>
<li>Show Memory Status:</br>
```
python app.py --show
```
</li>
</ol>