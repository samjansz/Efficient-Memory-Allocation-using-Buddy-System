from app import BuddySystem

buddy_system = BuddySystem(1024, 16)

def test_one():
    print("\nTest 1: Initialization")
    buddy_system.display_memory()

test_one()
def test_two():
    print("\nTest 2: Single Large Allocation")
    buddy_system.allocate(512)
    buddy_system.display_memory()

def test_three():
    print("\nTest 3: Multiple Small Allocations")
    buddy_system.allocate(128)
    buddy_system.allocate(64)
    buddy_system.allocate(32)
    buddy_system.allocate(16)
    buddy_system.display_memory()

def test_four():
    print("\nTest 4: Over-allocation")
    buddy_system.allocate(2048)

def test_five():
    print("\nTest 5: Smallest Block Allocation")
    buddy_system.allocate(16)
    buddy_system.display_memory()

def test_six():
    print("\nTest 6: Deallocation and Merging")
    buddy_system.allocate(128)
    buddy_system.deallocate(0)
    buddy_system.deallocate(128)
    buddy_system.display_memory()

def test_seven():
    print("\nTest 7: Allocate After Deallocate")
    buddy_system.allocate(128)
    buddy_system.deallocate(0)
    buddy_system.allocate(256)
    buddy_system.display_memory()

def test_eight():
    print("\nTest 8: Full Allocation and Deallocation")
    for _ in range(4):  # Allocate 4 blocks of 256 KB each
        buddy_system.allocate(256)
    buddy_system.display_memory()
    for i in range(0, 1024, 256):  # Deallocate all blocks
        buddy_system.deallocate(i)
    buddy_system.display_memory()
test_eight()