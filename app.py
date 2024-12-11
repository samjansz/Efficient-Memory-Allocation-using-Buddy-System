import argparse

#Node class to represent each memory block.
class Node:
    def __init__(self, size, start_address=0):
        self.size = size
        self.start_address = start_address
        self.is_free = True
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node(size={self.size}, start_address={self.start_address}, is_free={self.is_free})"


#Buddy System Manager to tracks the entire memory hierarchy
class BuddySystem:
    def __init__(self, total_size, min_block_size):
        self.root = Node(total_size)
        self.min_block_size = min_block_size
        print(f"Initialized Buddy System with {total_size} KB total memory and {min_block_size} KB minimum block size.")
    
    #Memory Allocation
    def allocate(self, size):
        if size > self.root.size:
            print("Error: Requested size exceeds total memory.")
            return None
        request_size = max(self.min_block_size, self._next_power_of_two(size))
        allocated_block = self._allocate_block(self.root, request_size)
        if allocated_block:
            print(f"Allocated {request_size} KB at address {allocated_block.start_address}")
        else:
            print("Error: Not enough memory to allocate.")
        return allocated_block

    def _allocate_block(self, node, size):
        if node.size < size:
            print(f"Skipping block: {node.size} KB (too small)")
            return None
        if node.size == size and node.is_free:
            print(f"Allocating block: {node.size} KB at address {node.start_address}")
            node.is_free = False
            return node
        # If the node has children, check them for allocation
        if node.left or node.right:
            allocated = self._allocate_block(node.left, size)
            if allocated:
                return allocated
            return self._allocate_block(node.right, size)
        # If the node has no children, split it and try again
        self._split(node)
        return self._allocate_block(node, size)

    def _split(self, node):
        if node.left or node.right:
            return
        half_size = node.size // 2
        node.left = Node(half_size, node.start_address)
        node.right = Node(half_size, node.start_address + half_size)
        node.is_free = False 
        print(f"Split {node.size} KB block into two {half_size} KB blocks.")

    def _next_power_of_two(self, n):
        # Find the next power of two greater than or equal to n
        power = 1
        while power < n:
            power *= 2
        return power


    def display_memory(self, node=None, level=0):
        # Display the memory tree structure
        if node is None:
            node = self.root
        print(" " * (level * 4) + f"Block: {node.size} KB, Free: {node.is_free}")
        if node.left:
            self.display_memory(node.left, level + 1)
        if node.right:
            self.display_memory(node.right, level + 1)


    # Memory Deallocation
    def deallocate(self, start_address):
        if not self._deallocate_block(self.root, start_address):
            print(f"Error: No allocated block found at address {start_address}")
        else:
            print(f"Deallocated block at address {start_address}")

    def _deallocate_block(self, node, start_address):
        if node is None:
            return False
        # Prevent root block from being freed unless explicitly allocated
        if node == self.root and node.start_address == start_address and not node.is_free:
            print(f"Freeing root block: {node.size} KB at address {node.start_address}")
            node.is_free = True
            return True
        # Free the matching block
        if node.start_address == start_address and not node.is_free:
            print(f"Freeing block: {node.size} KB at address {node.start_address}")
            node.is_free = True
            self._merge(node)
            return True
        # Search recursively in the left and right children
        return (
            self._deallocate_block(node.left, start_address) or 
            self._deallocate_block(node.right, start_address)
        )

    def _merge(self, node):
        # Merge two buddies if both are free
        if node.left and node.right and node.left.is_free and node.right.is_free:
            print(f"Merging blocks: {node.left.size} KB and {node.right.size} KB into {node.size} KB")
            node.left = None  
            node.right = None  
            node.is_free = True  

        # Recursively attempt to merge upward
        parent = self._find_parent(self.root, node)
        if parent and parent.left and parent.right and parent.left.is_free and parent.right.is_free:
            self._merge(parent)

    def _find_parent(self, current, child):
        # Find the parent of a given node
        if current is None or (current.left == child or current.right == child):
            return current

        # Search in the left or right subtree
        left_search = self._find_parent(current.left, child)
        if left_search:
            return left_search
        return self._find_parent(current.right, child)

    # Display memory tree structure
    def display_memory(self, node=None, level=0):
        if node is None:
            node = self.root
        print(" " * (level * 4) + f"Block: {node.size} KB, Free: {node.is_free}")
        if node.left:
            self.display_memory(node.left, level + 1)
        if node.right:
            self.display_memory(node.right, level + 1)



def run_cli():
    parser = argparse.ArgumentParser(description="Buddy System Memory Management CLI")

    parser.add_argument('-a', '--allocate', type=int, help="Allocate memory of specified size in KB")
    parser.add_argument('-d', '--deallocate', type=int, help="Deallocate memory at specified address")
    parser.add_argument('-s', '--show', action='store_true', help="Display current memory status")

    args = parser.parse_args()

    buddy_system = BuddySystem(1024, 16)

    if args.allocate:
        buddy_system.allocate(args.allocate)
    elif args.deallocate:
        buddy_system.deallocate(args.deallocate)
    elif args.show:
        buddy_system.display_memory()
    else:
        parser.print_help()

if __name__ == '__main__':
    run_cli()
    
#python app.py --allocate 100
#python app.py --deallocate 0
#python app.py --show
