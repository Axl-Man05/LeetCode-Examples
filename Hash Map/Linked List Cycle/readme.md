# Linked List Cycle

## Problem Description
Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. 

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

## Approach: Two Pointers (Floyd's Tortoise and Hare)

Although this problem is categorized under "Hash Map", the implementation uses an even more optimal approach: **Two Pointers**. This is widely known as Floyd's Cycle-Finding Algorithm.

### Explanation
1. We initialize two pointers, `slow` and `fast`, both pointing to the `head` of the list.
2. We move `slow` one step at a time (`slow = slow.next`), and `fast` two steps at a time (`fast = fast.next.next`).
3. If there is no cycle, the `fast` pointer will eventually reach the end of the list (`None`), and we return `False`.
4. If there is a cycle, the `fast` pointer will eventually "lap" the `slow` pointer, meaning `fast == slow`. When they meet, we return `True`.

### Complexity Analysis
- **Time Complexity:** $O(N)$ where $N$ is the number of nodes in the linked list. In the worst case, the fast pointer might have to traverse the cycle a few times, but it will always meet the slow pointer in linear time.
- **Space Complexity:** $O(1)$. We only use two pointers (`slow` and `fast`), regardless of the size of the linked list. This is much more efficient in terms of memory than the Hash Set approach!

## Local Execution vs LeetCode
El archivo `linkedListCycle.py` está escrito **exactamente** como se debe pegar en LeetCode. No contiene los imports de `Optional` ni la definición de `ListNode` porque LeetCode ya los inyecta por detrás.

Para poder ejecutar los tests localmente sin modificar el archivo original, hemos extraído la clase `ListNode` en su propio archivo (`list_node.py`). En el archivo de tests, inyectamos estas dependencias de forma dinámica para que Python no falle al intentar importar tu código.

## Testing Setup (For Beginners)

Testing linked list problems can seem intimidating because you need to manually construct the linked list and, in this case, artificially create a cycle. 

However, **it is highly recommended to implement these tests**. Building the helper functions to create the lists will greatly improve your understanding of how linked lists work under the hood.

In the `test_linkedListCycle.py` file, we have implemented two helper functions:
1.  `create_linked_list(values)`: Takes a normal Python list (array) and turns it into a proper Linked List using the `ListNode` class.
2.  `create_cycle(head, pos)`: Takes the head of a linked list and an index (`pos`). It loops through the list and connects the tail's `next` pointer back to the node at index `pos`, effectively creating the cycle for testing.

### Running the tests
You can run the tests using `pytest`. Ensure you have it installed:
```bash
pip install pytest
```

Then run the tests in the terminal from this directory:
```bash
pytest test_linkedListCycle.py -v
```
